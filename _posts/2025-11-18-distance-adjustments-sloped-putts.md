---
title: "Effective Distance on Sloped Greens"
layout: post
author: Stephen Lee
categories: [golf, physics]
tags: [golf, physics, putting, aimpoint]
toc: true
katex: true
---

## The Problem

You face a 20-foot putt that's 2% downhill on 10-stimp greens. How hard should you hit it?

Instead of thinking "hit it softer than a flat 20-footer," what if we could translate this into an equivalent flat distance? Your body already knows how to hit a 15-footer—that muscle memory is far more reliable than abstract "softer" adjustments.

## Derivation

From [previous posts]({% post_url 2025-11-17-rederiving-aimpoint %}), we know that for a putt with total rollout $$L = D + R$$, the required initial velocity is:

$$
v_0^2 = 2 a_{\text{eff}} L
$$

where $$a_{\text{eff}}$$ is the effective deceleration accounting for both friction and slope.

**Deceleration from Friction**

On flat greens at Stimp $$S$$:

$$
a_f = -\frac{v_s^2}{2S} \approx -\frac{19.7}{S}
$$

where $$v_s \approx 6.27\ \text{ft/s}$$ is the Stimp meter release velocity.

**Acceleration from Gravity**

On a slope with forward grade $$X$$ (positive uphill, negative downhill), gravity adds:

$$
a_g = \frac{5}{7} g X \approx 23 X
$$

The effective deceleration becomes:

$$
a_{\text{eff}} = a_f + a_g \approx -\frac{19.7}{S} - 23X
$$

**Distance Adjustment**

To find the equivalent flat distance, we set initial velocities equal:

$$
-\frac{19.7}{S} \cdot 2 L_{\text{flat}} = -\left(\frac{19.7}{S} + 23X\right) \cdot 2 L_{\text{slope}}
$$

Solving for $$L_{\text{flat}}$$:

$$
L_{\text{flat}} = \left(1 + \frac{23SX}{19.7}\right) L_{\text{slope}}
$$

Using $$\frac{23}{19.7} \approx 1.17$$:

$$
\frac{L_{\text{flat}}}{L_{\text{slope}}} =  1 + 1.17 \, S \, X
$$

This is our distance adjustment formula.

## The Tables

### Effective Distance 

Multiply your actual distance by these percentages:

| Forward Slope | Stimp 8 | Stimp 9 | Stimp 10 | Stimp 11 | Stimp 12 |
|--------------|---------|---------|----------|----------|----------|
| +3% (steep uphill) | 128% | 132% | 135% | 139% | 142% |
| +2% (uphill) | 119% | 121% | 123% | 126% | 128% |
| +1% (slight uphill) | 109% | 111% | 112% | 113% | 114% |
| 0% (flat) | 100% | 100% | 100% | 100% | 100% |
| -1% (slight downhill) | 91% | 89% | 88% | 87% | 86% |
| -2% (downhill) | 81% | 79% | 77% | 74% | 72% |
| -3% (steep downhill) | 72% | 68% | 65% | 61% | 58% |

**Example:** 20-foot putt, 2% downhill, 10 stimp → $$20 \times 0.77 = 15.4$$ feet

### 10-Foot Putt

| Forward Slope | Stimp 8 | Stimp 10 | Stimp 12 | Stimp 14 |
|--------------|---------|----------|----------|----------|
| +3% (steep uphill) | 12.8 ft | 13.5 ft | 14.2 ft | 14.9 ft |
| +2% (uphill) | 11.9 ft | 12.3 ft | 12.8 ft | 13.3 ft |
| +1% (slight uphill) | 10.9 ft | 11.2 ft | 11.4 ft | 11.6 ft |
| 0% (flat) | 10.0 ft | 10.0 ft | 10.0 ft | 10.0 ft |
| -1% (slight downhill) | 9.1 ft | 8.8 ft | 8.6 ft | 8.4 ft |
| -2% (downhill) | 8.1 ft | 7.7 ft | 7.2 ft | 6.7 ft |
| -3% (steep downhill) | 7.2 ft | 6.5 ft | 5.8 ft | 5.1 ft |

## Key takeaways

1. **Faster greens amplify slope effects.** On 14-stimp greens, a 3% uphill 10-footer plays like 15 feet (+49%), while 3% downhill plays like 5 feet (-49%). On 8-stimp greens, the same slopes only adjust ±28%. Speed matters.

2. **Downhill adjustments are more dramatic than uphill.** A 2% downhill putt on 10-stimp greens requires hitting 77% of the distance—a 20-footer becomes a 15-footer. But 2% uphill only requires 123%—a 20-footer becomes 24.5 feet. You lose more distance downhill than you gain uphill.

## How to Use This

It's simple:

1. Read your slope (e.g., 2% uphill)
2. Know the green speed (e.g., 10 stimp)
3. Look up the adjustment (e.g., 123%)
4. Hit it like the adjusted distance (e.g., 20 × 1.23 = 24.6 feet)

That's it. Your body knows what a 25-footer feels like. Trust that muscle memory instead of guessing "hit it harder."

On the practice green, verify the table matches your feel. Hit 10-footers at different slopes and see if the adjustments work. Once calibrated, you'll have a reliable system for speed control.

---
