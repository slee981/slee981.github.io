---
layout: post
author: Stephen Lee
title: "Calibrating Aimpoint Express"
categories: [golf, physics]
tags: [golf, physics, putting, aimpoint, geometry]
toc: true
katex: true
---

## Introduction 

In my [previous post]({% post_url 2025-11-16-rederiving-aimpoint %}), I derived a simple physical model to estimate how many inches a putt breaks on sloped greens. Next, we're going to derive some calibration rules behind the famous (infamous?) Aimpoint Express finger-reading system.

The Express method is elegant and simple: 

1. Stand just above/behind the ball, 
1. Hold up X fingers for X% side slope (one per percent of side slope), 
1. Close your non-dominant eye, 
1. Align one side of your finger with the center of the hole such that the rest of the finger(s) covers the edge of 
    the cup in the direction you'd need to start your putt. 
1. Observe the location where you can first see grass that is parallel with the center of the hole.

This spot becomes your "aim point", and you then just pretend to hit a dead straight putt at that point. 

## Problem 

The magic of this system is in the calibration: how far should you hold your hand from your face?

It turns out the answer involves elegant geometry and depends critically on both green speed and the slope uphill or downhill.

## The Triangle Geometry

The Aimpoint Express system works through similar triangles:

$$
\frac{\text{Finger Width } (w)}{\text{Viewing Distance } (L)} = \frac{\text{Break at Hole } (B)}{\text{Distance to Hole } (D)}
$$

Rearranging:

$$
B = \frac{w \cdot D}{L}
$$

The key insight: if break is linear in distance, then we can choose a fixed viewing distance $$L$$ inches away from our face that works for all putt lengths.

## Why This Works

From the [previous derivation]({% post_url 2025-11-16-rederiving-aimpoint %}), the physics model gives break as a function of distance with a $$(\sqrt{D+R} - \sqrt{R})^2$$ term, where $$D$$ is the distance to the hole and $$R$$ is the additional roll out distance the ball would travel if you didn't make the putt. 

For practical estimates with small roll out distance (e.g. you hit a 10 footer with enough speed to go 11ft), this break is very nearly linear in distance to the hole.

To verify this, I fit a simple linear model:

$$
B \approx \alpha \cdot D
$$

where the value of $$\alpha$$ depends on:
- Green speed (Stimp reading)
- Side slope percentage
- Forward slope percentage

We will see that this simple linear approximation fits extremely well with our model from the previous post ($$R^2 > 0.99$$), which means for a given putt (fixed green speed and slopes), we can treat $$\alpha$$ as constant. 

Therefore:

$$
\frac{w}{L} = \alpha \quad \Rightarrow \quad L = \frac{w}{\alpha}
$$

This means the viewing distance away from your face $$L$$ is constant for any given green speed, side slope, and forward slope combination. You don't need to adjust for putt distance - the similar geometry scales it automatically!

## "N" Fingers 

Here's another elegant consequence: if side slope doubles (say, 1% → 2%), the break doubles:

$$
B_{2\%} = 2 \times B_{1\%}
$$

So for 2% slope, you hold up two fingers with the same width $$2w$$:

$$
\frac{2w}{L} = 2\alpha
$$

The viewing distance stays exactly the same. This is why the Express system scales so well. You just use more fingers for steeper side slopes and keep your hand at the same calibrated distance.

## Calibration

The approach is straightforward but elegant. For each combination of green speed and slope conditions, I need to find the coefficient $$\alpha$$ that describes how break scales with distance. Then $$L = w / \alpha$$ gives the viewing distance you need to hold your fingers from your face.

Here's the process:

**Step 1: Generate data**

I used the dampened break model from the previous post to calculate expected break for:
- Stimp values: 8, 10, 12, 14
- Forward slopes: -3%, -2%, -1%, 0%, +1%, +2%, +3%
- Side slope: 1% (other slopes scale proportionally)
- Distances: 3-30 feet (in 1-foot increments)
- Rollout: 1.5 feet past the hole

This creates 756 observations (4 Stimp × 7 forward slopes × 27 distances).

**Step 2: Fit linear models**

For each Stimp value, I estimate a regression model with separate slope coefficients for each forward slope condition (since the uphill/downhill changes the speed, and consequently, the break). Using indicator variables $$\mathbb{1}_{j}$$ for each of the $$j=1,...,7$$ forward slope categories:

$$
B_ij = \sum_{j=1}^{7} \alpha_j \cdot \mathbb{1}_{j} \cdot D_i + \epsilon_i
$$

where:
- $$B_ij$$ is the specific putt's break in inches.
- $$D_i$$ is the putt's distance to the hole in feet.
- $$\alpha_j$$ is the coefficient (inches of break per foot) for a given slope uphill or downhill.
- $$\epsilon_i$$ is the error term that our linear model doesn't capture. 

This gives us 7 coefficients per Stimp value (one for each forward slope).

**Step 3: Extract viewing distances**

From the regression coefficients, we use our fitted parameters to reverse engineer what viewing distance from your face you should hold your fingers:

$$
L = \frac{w}{\alpha}
$$

where $$w$$ is your finger width (e.g. mine is about 0.75 inch).

## Results

Here are the viewing distances (the number of inches you should hold your fingers from your face):

| Forward Slope | Stimp 8 | Stimp 10 | Stimp 12 | Stimp 14 |
|--------------|---------|----------|----------|----------|
| -3% (steep downhill) | 10" | 7" | 5" | 4" |
| -2% (downhill) | 11" | 8" | 7" | 5" |
| -1% (slight downhill) | 12" | 10" | 8" | 7" |
| 0% (flat) | 14" | 11" | 9" | 8" |
| +1% (slight uphill) | 15" | 12" | 10" | 9" |
| +2% (uphill) | 16" | 13" | 12" | 10" |
| +3% (steep uphill) | 17" | 15" | 13" | 12" |

The regression fits are excellent ($$R^2 = 0.992$$), confirming that break really is linear in distance.

## Key Insights

1. **Uphill/Downhill Slope Requires Adjustment**

    This was actually my initial motivation for the analysis as the videos I saw online didn't really talk much about how to adjust the Express system for uphill/downhill slopes. I guess that's the paywalled version! 

    What I find is that the viewing distance changes nearly 1 inch per percent of forward slope:
    - Downhill: hold fingers closer (more break)
    - Uphill: hold fingers farther (less break)

    On its own, not a huge deal, but when you compare a 10 footer with 2% side slope that is 2% uphill vs. 2% downhill, my estimates show about 7 inches of total break difference! If you're not even trying to move your fingers closer/farther from your face, you will miss. 

2. **The Express System is Excellent**

    All of the physics here validates that the simple fingers approach truly provides a consistent and useful heuristic for estimating total break. 

    The massive caveat (and reason for all this work), is that calibrating the distance to hold your fingers is really important, and adjusting for uphill/downhill can make or break you. 

## Application

To use this on the course:

1. Assess green speed. Ask the pro shop for the Stimp reading, or estimate based on course conditions
1. Read the forward slope. Is your putt uphill, downhill, or flat?
1. Read the side slope. 
1. Find your viewing distance. Use the table above for a starting point. 
1. Hold up fingers. One per percent, at the correct viewing distance.
1. Find your aim point. 

## Conclusion

The Aimpoint Express finger-reading system embodies elegant applied physics. The similar-triangle geometry, combined with the linear break-distance relationship, creates a practical tool that scales naturally with slope percentage.

The calibration table reveals why green-reading feels so different across course conditions: on fast greens with downhill putts, you need to hold your hand quite close to see the correct break angle. On slower, uphill putts, extend your arm farther.

Next time you're on the practice green, find the Stimp reading and test these viewing distances. I suspect you'll find they provide an excellent baseline for the Express system—and a deeper appreciation for the physics happening beneath your feet.

---
