---
title: Modeling Aimpoint for Green Reading
layout: post
author: Stephen Lee

toc: true
katex: true
categories: [golf, physics]
tags: [golf, physics]
---


# The Physics of Putting

## Problem 

Aimpoint Express is a common system for calibrating your feet and fingers to estimate the break of a putt. Tune in to a professional golf tournament and you're likely to see players doing funny things with their fingers, and awkwardly straddling their line. 

I played competitive golf for many years, but tended to hit it better tee to green than I could consistently putt. This post is an attempt to better understand the physics of how putts break, and perhaps more importantly, how green speed and uphill/downhill slopes impact that break. 

This first part lays out the foundation for a simple model that estimates how far a ball rolls and how much it breaks. The goal isn't to produce a full dynamics treatment or handle every edge case. Instead, we want something accurate in the practical range where golfers actually need precision: putts of about 5–20 feet on slopes of roughly 0–3%.

We'll start by recalling a few Newtonian relationships, connect them to the Stimp reading, and show how slope influences both speed and break.

## Newton's Laws

A rolling ball on a green slows down at a roughly constant rate due to rolling friction. Because the speeds and slopes involved are small, this constant-acceleration approximation works well for short putts.

Under constant acceleration, there are three relationships we'll use:[^1]

1. $$ v(t) = v_0 + a t $$

2. $$ s(t) = v_0 t + \frac{1}{2} a t^2 $$

3. $$v^2 = v_0^2 + 2 a s$$

For putting, the third equation is especially convenient because the ball always ends with $$v = 0$$. That gives a direct link between the initial speed, the deceleration, and the stopping distance.

---

## Stimpmeters

A Stimp reading $$S$$ is the distance (in feet) that a golf ball rolls on a level green after being released from a standard Stimp meter. The USGA-specified Stimp meter is a 30-inch long aluminum bar with a V-groove. A ball is placed in a notch and the bar is slowly raised until the ball releases when the angle reaches approximately 20 degrees.

### Exit Velocity

When a golf ball rolls down the Stimp meter ramp without slipping, its acceleration is reduced by rotational inertia. A sliding object on an incline accelerates at $$g\sin\theta$$, but a rolling sphere must also spin up, which "costs" kinetic energy. For a solid sphere with moment of inertia $$I = \frac{2}{5}mR^2$$, this reduces the acceleration by a factor of $$\frac{7}{5}$$:[^2]

$$
a = \frac{5g\sin\theta}{7}
$$

For the USGA Stimp meter with $$\theta = 20°$$ and $$g = 32.17\ \text{ft/s}^2$$:

$$
a = \frac{5 \times 32.17 \times \sin(20°)}{7} \approx 7.87\ \text{ft/s}^2
$$

The ball rolls down $$L = 30\ \text{in} = 2.5\ \text{ft}$$ starting from rest. Using $$v^2 = v_0^2 + 2as$$ with $$v_0 = 0$$:

$$
v_s = \sqrt{2aL} = \sqrt{2 \times 7.87 \times 2.5} \approx 6.27\ \text{ft/s}
$$

This exit velocity is the key to connecting the Stimp reading to green speed.

### Frictional Deceleration

Using the velocity–position relation with $$v = 0$$:

$$
0 = v_s^2 + 2 a_f S
$$

Solving for the frictional deceleration $$a_f$$:[^3]

$$
a_f = -\frac{v_s^2}{2 S}
$$

This tells us:

- Faster greens (larger Stimp numbers) have **smaller magnitude deceleration**.
- Slower greens have **larger deceleration**.

Everything else in this model builds off that simple relationship.

For example, on greens that stimp 10, we find that the greens slow the ball down: 

$$
a_f \approx -\frac{6.27^2}{2 \cdot 10} = -1.97 \frac{ft}{s^2}
$$



---

## Slope and Speed

Now consider an uphill or downhill slope. On a slope with rise/run ratio $$X$$, the component of gravity along the slope direction is $$g\sin\theta$$. For small angles (typical on greens), $$\sin\theta \approx \tan\theta = X$$, giving:

$$
a_g \approx g X
$$

where:

- $$X$$ is slope expressed as a decimal (e.g., 2% = 0.02, positive for uphill, negative for downhill)
- $$g = -32.17\ \mathrm{ft/s^2}$$

Since friction $$a_f$$ is negative (opposing motion), the total acceleration becomes:

$$
a_\text{eff} = a_f + a_g < 0
$$

More explicitly:

- Downhill: $$X < 0, \text{which implies } a_g > 0$$. Negative slope causes the ball to lose speed slower i.e. it decreases the magnitude of deceleration. 
- Uphill: $$X > 0, \text{which implies } a_g < 0$$. Positive slope causes the ball to lose speed faster i.e. it increases the magnitude of deceleration.

Golfers often describe a slope as "making the putt faster or slower." Mathematically, this is the same as saying that the ball behaves as if the Stimp number changed.

Define $$S_{\text{eff}}$$ as the "effective Stimp" on the slope. Since $$S = -\frac{v_s^2}{2a_f}$$, the stopping distance is inversely proportional to the magnitude of deceleration:

$$
\frac{S_{\text{eff}}}{S} = \frac{a_f}{a_\text{eff}}
$$

After inserting constants and simplifying, we get a useful approximation:[^4]

$$
S_{\text{eff}} \approx \frac{S}{1 + 1.64 X S} 
$$



where the coefficient 1.64 comes from $$\frac{2g}{v_s^2}$$ with $$g = 32.17\ \text{ft/s}^2$$ and $$v_s \approx 6.27\ \text{ft/s}$$ (the exit velocity from a USGA Stimp meter).

This provides a practical way to think about uphill or downhill putts without re-deriving the full dynamics.

---

## Slope and Break

The same slope that changes speed can also produce lateral acceleration when the slope tilts sideways relative to the target line.

**Note:** When calculating break, we need to account for the *effective* Stimp $$S_\text{eff}$$ from Section 3 so any uphill or downhill slope factors in to the time the putt has to move sideways. This way, a putt going uphill (which actually stops in a shorter amount of time) will have less time to break laterally.

Let $$X_s$$ be the side-slope (in decimal form). The lateral component of gravitational acceleration is:

$$
a_\text{lat} = g X_s
$$

**Important:** We want to calculate the lateral displacement **at the hole** (distance $$D$$), not at the final stopping point. The golfer needs to know how much the ball breaks by the time it reaches the cup, even though it has enough speed to roll past.

### Break at the Hole

To compute the break at distance $$D$$, we need to find how long it takes the ball to reach the hole when it has enough speed to roll out a total distance $$L = D + R$$, where:

- $$D$$ = distance to the hole
- $$R$$ = desired rollout past the hole (e.g. 1 foot or so)

**Step 1:** The initial speed needed to roll total distance $$L = D + R$$ is:

$$
v_0 = \sqrt{2 a_\text{eff} (D+R)}
$$

**Step 2:** The time to reach the hole at distance $$D$$ (not the stopping time!) satisfies:

$$
D = v_0 t_D - \frac{1}{2}a_\text{eff} t_D^2
$$

Solving this quadratic gives:

$$
t_D = \frac{v_0 - \sqrt{v_0^2 - 2 a_\text{eff} D}}{a_\text{eff}}
$$

Substituting $$v_0^2 = 2  a_\text{eff} (D+R)$$:

$$
t_D = \frac{\sqrt{2a_\text{eff}(D+R)} - \sqrt{2a_\text{eff} R}}{a_\text{eff}}
    = \sqrt{\frac{2}{a_\text{eff}}}\left(\sqrt{D+R} - \sqrt{R}\right)
$$

**Step 3:** Lateral displacement at the hole becomes:

$$
x_\text{break} = \frac{1}{2} a_\text{lat} t_D^2
               = \frac{g X_s}{a_\text{eff}}\left(\sqrt{D+R} - \sqrt{R}\right)^2
$$

Now substitute the physical relationship for effective deceleration. The ball experiences both friction and gravity along the forward direction:

$$
a_\text{eff} = a_f + a_g \approx -( \frac{6.27^2}{2S} + gX)
$$

where $$X$$ is the forward slope (positive uphill, negative downhill). 

Substituting everything in:

$$
x_\text{break} \approx \frac{g X_s S}{19.7 + g S X}\left(\sqrt{D+R} - \sqrt{R}\right)^2
$$

This is now the break in feet. We simply multiply by 12 to get break in inches: 

$$
x_\text{break} \approx \frac{12 g X_s S}{19.7 + g S X}\left(\sqrt{D+R} - \sqrt{R}\right)^2
$$

This makes the dependence on base Stimp and forward slope explicit without needing to first calculate effective Stimp.

### Friction Damping of Break

This model treats lateral and forward motion independently—gravity accelerates the ball laterally while friction only decelerates it forward. In reality, friction opposes the *total* velocity vector (the vector sum of forward and lateral components), which reduces lateral deflection somewhat. In other words, the problem really needs to be modeled with velocity as a 3D vector that changes over time, and friction would produce an acceleration that opposes that motion.

But our goal is a useful model that generates accurate heuristics for players on the course. A simple correction is to multiply the break by some damping factor. We'll use $$f_\text{damp} \approx \frac{5}{7}$$, analogous to how rotational inertia reduces forward acceleration. While not rigorously derived from the coupled dynamics, this heuristic gives a practical first-order correction:

$$
x_\text{break,damped} \approx \frac{5}{7} \left(\frac{12 g X_s S}{19.7 + g S X} \right) \left(\sqrt{D+R} - \sqrt{R}\right)^2
$$

This captures the essential behavior of a breaking putt under the assumptions of constant friction and small slopes.

## Results 

How does this model perform? 

### Effective Stimp

First, we'll analyze a table of effective Stimps on different slopes: 

| Forward Slope (%) | S = 8 | S = 9 | S = 10 | S = 11 | S = 12 |
|:-----------------:|:-----:|:-----:|:------:|:------:|:------:|
|        +3         |  5.7  |  6.2  |  6.7   |  7.1   |  7.5   |
|        +2         |  6.3  |  6.9  |  7.5   |  8.1   |  8.6   |
|        +1         |  7.1  |  7.8  |  8.6   |  9.3   |  10.0  |
|         0         |  8.0  |  9.0  |  10.0  |  11.0  |  12.0  |
|        -1         |  9.2  | 10.6  |  12.0  |  13.4  |  14.9  |
|        -2         | 10.8  | 12.8  |  14.9  |  17.2  |  19.8  |
|        -3         | 13.2  | 16.2  |  19.7  |  24.0  |  29.3  |

This is very much in line with what old Aimpoint charts presented. You can still find those floating around online if you look. 


### 1% side slope

To evaluate the total break, we need to pick a green speed and a side slope. For greens that run 10 on the Stimp, this model produces the following estimates for total break. 

  | Forward Slope (%) | D = 3 | D = 5 | D = 10 | D = 15 | D = 20 | D = 30 |
  |:-----------------:|:-----:|:-----:|:------:|:------:|:------:|:------:|
  |        +3         |  0.8  |  1.6  |  4.4   |  7.6   |  10.9  |  18.1  |
  |        +2         |  0.8  |  1.9  |  5.0   |  8.5   |  12.3  |  20.3  |
  |        +1         |  1.0  |  2.1  |  5.6   |  9.7   |  14.0  |  23.2  |
  |         0         |  1.1  |  2.5  |  6.6   |  11.3  |  16.3  |  26.9  |
  |        -1         |  1.3  |  2.9  |  7.9   |  13.5  |  19.5  |  32.2  |
  |        -2         |  1.7  |  3.6  |  9.8   |  16.7  |  24.2  |  40.0  |
  |        -3         |  2.2  |  4.8  |  12.9  |  22.1  |  31.9  |  52.8  |

**Note**, these values can be interpreted as total break. But remember, since the cup is just over 4 inches in diameter, the breaks of 1 that you see will still be played inside the edge of the cup. 

### 2% side slope 

  | Forward Slope (%) | D = 3 | D = 5 | D = 10 | D = 15 | D = 20 | D = 30 |
  |:-----------------:|:-----:|:-----:|:------:|:------:|:------:|:------:|
  |        +3         |  1.5  |  3.3  |  8.8   |  15.1  |  21.9  |  36.2  |
  |        +2         |  1.7  |  3.7  |  9.9   |  17.0  |  24.6  |  40.6  |
  |        +1         |  1.9  |  4.2  |  11.3  |  19.4  |  28.0  |  46.3  |
  |         0         |  2.3  |  4.9  |  13.1  |  22.5  |  32.6  |  53.9  |
  |        -1         |  2.7  |  5.9  |  15.7  |  26.9  |  39.0  |  64.4  |
  |        -2         |  3.3  |  7.3  |  19.5  |  33.5  |  48.4  |  80.0  |
  |        -3         |  4.4  |  9.6  |  25.8  |  44.2  |  63.9  | 105.7  |

### 3% side slope 

  | Forward Slope (%) | D = 3 | D = 5 | D = 10 | D = 15 | D = 20 | D = 30 |
  |:-----------------:|:-----:|:-----:|:------:|:------:|:------:|:------:|
  |        +3         |  2.3  |  4.9  |  13.2  |  22.7  |  32.8  |  54.3  |
  |        +2         |  2.5  |  5.6  |  14.9  |  25.5  |  36.9  |  60.9  |
  |        +1         |  2.9  |  6.3  |  16.9  |  29.1  |  42.0  |  69.5  |
  |         0         |  3.4  |  7.4  |  19.7  |  33.8  |  48.9  |  80.8  |
  |        -1         |  4.0  |  8.8  |  23.6  |  40.4  |  58.4  |  96.6  |
  |        -2         |  5.0  | 10.9  |  29.3  |  50.2  |  72.6  | 120.1  |
  |        -3         |  6.6  | 14.4  |  38.6  |  66.3  |  95.8  | 158.5  |

---

## Summary 

These values are very much in line with what official aimport charts, and newer Aimpoint Express generate. 

While I don't personally plan to, or even recommend, using charts like this on the course, the excerise of modeling this out was instructive to conclude: 

1. **Faster greens are much more demanding on speed control**. Uphill putts are relatively slower, and downhill putts much faster than the same grade slope on slower greens. In other words, the faster the greens, the smaller margin of error you have in every way speed wise. I didn't show the calculation, but if you examine the relative increase/decrease in effective Stimp compared to true Stimp, the faster greens are more extreme percent changes both up and down hill. 

2. **Break increases (or decreases) porportional to the increase (or decrease) in speed**. If you have a fast downhill putt, it may act like a green that is nearly 2x as fast! But importantly, it will break 2x as much as your read would tell you if you only look at side slope. The reverse is true with uphill putts. 

3. **Aimpoint Express is really a great system**. But spend the time to calibrate your feelings with your feet, and give as much attention to the uphill/downhill slope as you do the side slope. 

## Appendix

This appendix provides step-by-step derivations for the key equations used in the main text.

### A0. Newton's Laws {#appendix-kinematics}

[^1]: See [Appendix A0](#appendix-kinematics) for the full derivation from calculus.

We start with the fundamental definitions of velocity and acceleration as derivatives:

$$
v(t) = \frac{ds}{dt} \quad \text{and} \quad a(t) = \frac{dv}{dt}
$$

For constant acceleration, $$a(t) = a$$ (a constant value).

**Equation 1: $$v(t) = v_0 + at$$**

Starting with the definition of acceleration:

$$
\frac{dv}{dt} = a
$$

Integrate both sides with respect to time:

$$
\int dv = \int a \, dt
$$

$$
v = at + C
$$

Using the initial condition $$v(0) = v_0$$, we find $$C = v_0$$:

$$
v(t) = v_0 + at
$$

**Equation 2: $$s(t) = v_0 t + \frac{1}{2}at^2$$**

Starting with the definition of velocity and substituting our result from Equation 1:

$$
\frac{ds}{dt} = v(t) = v_0 + at
$$

Integrate both sides with respect to time:

$$
\int ds = \int (v_0 + at) \, dt
$$

$$
s = v_0 t + \frac{1}{2}at^2 + C
$$

Using the initial condition $$s(0) = 0$$ (measuring position from the starting point), we find $$C = 0$$:

$$
s(t) = v_0 t + \frac{1}{2}at^2
$$

**Equation 3: $$v^2 = v_0^2 + 2as$$**

We can derive this by eliminating time from Equations 1 and 2.

From Equation 1, solve for $$t$$:

$$
t = \frac{v - v_0}{a}
$$

Substitute into Equation 2:

$$
s = v_0 \left(\frac{v - v_0}{a}\right) + \frac{1}{2}a\left(\frac{v - v_0}{a}\right)^2
$$

$$
s = \frac{v_0(v - v_0)}{a} + \frac{1}{2a}(v - v_0)^2
$$

$$
s = \frac{v_0 v - v_0^2}{a} + \frac{v^2 - 2vv_0 + v_0^2}{2a}
$$

Multiply through by $$2a$$:

$$
2as = 2v_0 v - 2v_0^2 + v^2 - 2vv_0 + v_0^2
$$

$$
2as = v^2 - v_0^2
$$

Rearranging:

$$
v^2 = v_0^2 + 2as
$$

**Alternative derivation using the chain rule:**

We can also derive Equation 3 more directly using the chain rule. Starting with:

$$
a = \frac{dv}{dt} = \frac{dv}{ds} \cdot \frac{ds}{dt} = v \frac{dv}{ds}
$$

Rearrange and integrate:

$$
a \, ds = v \, dv
$$

$$
\int_0^s a \, ds = \int_{v_0}^v v \, dv
$$

For constant $$a$$:

$$
as = \frac{1}{2}v^2 - \frac{1}{2}v_0^2
$$

$$
v^2 = v_0^2 + 2as
$$

### A1. Stimpmeter Exit Velocity {#appendix-stimp}

[^2]: See [Appendix A1](#appendix-stimp) for the calculation from USGA Stimp meter geometry.

The USGA Stimp meter is designed as a 30-inch (2.5 ft) inclined ramp with a V-groove. The ball is released from a notch when the angle reaches $$\theta \approx 20°$$.

When a ball rolls down an incline without slipping, it experiences:
- Gravitational component along the slope: $$g\sin\theta$$
- Rotational inertia effects that reduce the effective acceleration

For a sphere rolling without slipping down an incline, the acceleration is:

$$
a = \frac{g\sin\theta}{1 + \frac{I}{mR^2}}
$$

where $$I = \frac{2}{5}mR^2$$ for a solid sphere. This gives:

$$
a = \frac{g\sin\theta}{1 + \frac{2}{5}} = \frac{5g\sin\theta}{7}
$$

For $$\theta = 20°$$ and $$g = 32.17\ \text{ft/s}^2$$:

$$
a = \frac{5 \times 32.17 \times \sin(20°)}{7} \approx \frac{5 \times 32.17 \times 0.342}{7} \approx 7.87\ \text{ft/s}^2
$$

The ball rolls down a distance $$L = 2.5\ \text{ft}$$ (30 inches), starting from rest. Using $$v^2 = v_0^2 + 2as$$ with $$v_0 = 0$$:

$$
v_s^2 = 2 \times 7.87 \times 2.5 \approx 39.35
$$

$$
v_s \approx 6.27\ \text{ft/s}
$$

In practice, the exact release velocity depends on:
- The precise release angle (which varies slightly with operator technique)
- Any sliding that occurs before pure rolling begins
- The coefficient of friction in the V-groove

For most calculations, $$v_s \approx 6.0\ \text{ft/s}$$ is commonly used as a round approximation.

### A2. Frictional Deceleration {#appendix-friction}

[^3]: See [Appendix A2](#appendix-friction) for the full derivation.

Starting with the kinematic equation relating velocity, acceleration, and distance:

$$
v^2 = v_0^2 + 2as
$$

For a ball released from a Stimp meter:
- Initial velocity: $$v_0 = v_s$$ (the known Stimp meter release velocity)
- Final velocity: $$v = 0$$ (ball comes to rest)
- Distance traveled: $$s = S$$ (the Stimp reading)
- Acceleration: $$a = a_f$$ (the frictional deceleration we want to find)

Substituting these values:

$$
0^2 = v_s^2 + 2 a_f S
$$

$$
0 = v_s^2 + 2 a_f S
$$

Solving for $$a_f$$:

$$
-2 a_f S = v_s^2
$$

$$
a_f = -\frac{v_s^2}{2S}
$$

The negative sign indicates deceleration (acceleration opposite to the direction of motion).

### A3. Effective Stimp {#appendix-effective-stimp}

[^4]: See [Appendix A3](#appendix-effective-stimp) for the full derivation.

When the green has a slope $$X$$ (expressed as a decimal), gravity contributes an additional acceleration component:

$$
a_g = g X
$$

where $$g = 32.17\ \text{ft/s}^2$$ is gravitational acceleration.

The effective acceleration becomes:

$$
a_{\text{eff}} = a_f + a_g
$$

where $$a_f < 0$$ (friction opposes motion) and $$a_g = gX$$ (positive for downhill, negative for uphill).

The effective Stimp reading $$S_{\text{eff}}$$ is the distance a ball would roll with this modified acceleration. Using the same kinematic relationship:

$$
0 = v_s^2 + 2 a_{\text{eff}} S_{\text{eff}}
$$

$$
S_{\text{eff}} = -\frac{v_s^2}{2 a_{\text{eff}}}
$$

Taking the ratio with the level-green Stimp:

$$
\frac{S_{\text{eff}}}{S} = \frac{-\frac{v_s^2}{2 a_{\text{eff}}}}{-\frac{v_s^2}{2 a_f}} = \frac{a_f}{a_{\text{eff}}} = \frac{a_f}{a_f + gX}
$$

For a standard Stimp meter (as derived in Appendix A1), the release velocity is $$v_s \approx 6.27\ \text{ft/s}$$ and we can express $$a_f \approx \frac{19.7}{S}$$

$$
\frac{S_{\text{eff}}}{S} = \frac{a_f}{a_f + gX} = \frac{1}{1 + 1.64 X S}
$$

Therefore:

$$
S_{\text{eff}} \approx \frac{S}{1 + 1.64 X S} 
$$

---
