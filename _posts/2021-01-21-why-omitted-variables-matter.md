---
title: Omitted Variable Bias by Simulation
author: Stephen Lee
layout: post

categories: [econometrics, statistics]
tags: [R, stats, econometrics, prediction]
toc: true
katex: true
---

## Overview

In simulation, we can show that omitting a variable $$x_2$$ can cause the point estimates for a correlated variable $$x_1$$ to change from (positive) $$0.999$$ with a p-value of nearly zero, to (negative!) $$-0.512$$, also with a p-value of nearly zero! 

More generally, this reinforces the mantra that unless very specific assumptions are met, regression results should only be taken as linear predictors of an outcome, and not as a cause and effect relationship. Further, you cannot rely on statistical significance to guide you about whether your model is "well specified" or not. 

## Setup
You have data, and you're excited to use it. The only problem: you know the data is missing variables that you would prefer to have. 

Suppose we believe the variable $$x_1$$ predicts or explains an outcome $$y$$. Further, suppose there is an unobserved (or otherwise omitted) variable $$x_2$$, which is correlated with both $$y$$ and $$x_1$$. An immediate implication is that our error term will no longer independent of the included explanatory variable $$x_1$$, and our estimate of the relationship between $$x_1$$ and $$y$$ will be incorrect. 

More formally, suppose we have a "true" data generating process of

$$
y_{true} = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + u
$$

If we omit $$x_2$$ from our estimation and instead solve for the linear relationship 

$$
\hat{y} = \hat{\beta_0} + \hat{\beta_1} x_1 + e 
$$

Our point estimate for $$\hat{\beta_1}$$ will be misleading. We can see this mathematically as follows. If we solve the linear regression by ordinary least squares (OLS), then it can be shown that $$\hat{\beta}$$ is found by the relationship

$$
\hat{\beta} = (X^T X)^{-1}(X^T Y)
$$

Further, if we "de-mean" each variable by subtracting it's mean value from each observation, we find 

$$
\begin{aligned}
    \hat{\beta} &= \frac{\sum_i (x_i - \bar{x}) (y_i - \bar{y})}{\sum_i (x_i - \bar{x})^2} \\
    &= \frac{Cov(x, y)}{Var(x)}
\end{aligned}
$$

Speaking of omission, I will state without proof that this leads to the following relationship (for more details, see [this excellent PDF](https://are.berkeley.edu/courses/EEP118/spring2014/section/Handout5_student.pdf))

$$
\hat{\beta} = \beta + \frac{\sum_i (x_i - \bar{x}) e_i}{\sum_i (x_i - \bar{x}) x_i} 
$$

In this case, if we omit $$x_2$$, we can no longer expect that our error term will be zero conditional on some value of $$x$$. In other words, the condition $$E(e \lvert x) = 0$$ no longer holds. 

The takeaway here is that by omitting a relevant variable, $$\hat{\beta} \ne \beta$$. This is all well documented. 

## Question 
But I wonder: can we simulate this process to see how bad this bias can be? Further still, could this biased estimate still be "statistically significant"? 

## Answer

Yes, an omitted variable can flip the sign of your estimate of interest, and still appear significant. 

## Simulation 

To make this a bit more concrete, and to highlight the potential side-effects of unknown omitted variable bias, suppose we have a "true" data generating process of 

$$
\begin{aligned}
    y &= 4 + x_1 - 3x_2 + u \quad &u \sim N(0, 1) \\ \\
    x_2 &= 0.5x_1 + e \quad &e \sim N(0, 50) 
\end{aligned}
$$

Notice that $$x_2$$ is correlated with both $$y$$ and $$x_1$$. As such, if we don't include it in our regression model for whatever reason (either we don't observe it or don't think it's relevant), then we will actually estimate the relationship with the opposite sign, and both be statistically significant!

In code, we first create the simulation dataset:

```r
set.seed(981)    # <-- for random number generator

n <- 1000
 
x1 <- runif(n, -100, 100)
x2 <- 0.5 * x1 + rnorm(n, 0, 50)

y  <- 4 + x1 - 3*x2 + rnorm(n, 0, 1)

data <- tibble(
    y = y,
    x1 = x1,
    x2 = x2
)

# data
# # A tibble: 1,000 x 3
#         y     x1      x2
#     <dbl>  <dbl>   <dbl>
#  1 -130.  -67.4   22.4  
#  2 -112.   32.2   49.0  
#  3   80.0  16.5  -20.0  
#  4 -212.  -17.4   65.9  
#  5 -228.  -68.2   54.5  
#  6   67.0  60.3   -0.524
#  7   65.9  -2.55 -21.0  
#  8 -149.  -88.9   21.8  
#  9   91.8  20.0  -22.5  
# 10  -57.6  37.3   32.8  
# # … with 990 more rows
```

Next we can fit both the "true" and the "omitted" models. 

```r
# fit the models
fit_true    <- lm(y ~ x1 + x2)
fit_omitted <- lm(y ~ x1)
```

And finally, we view the results

```r
> #----------------------------------------------------------------
> # TRUE MODEL RESULTS
> summary(fit_true)

Call:
lm(formula = y ~ x1 + x2, data = data)

Coefficients:
              Estimate Std. Error t value Pr(>|t|)    
(Intercept)  3.9885178  0.0321514   124.1   <2e-16 ***
x1           0.9990703  0.0006465  1545.4   <2e-16 ***
x2          -2.9999153  0.0006280 -4776.9   <2e-16 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 1.016 on 997 degrees of freedom
Multiple R-squared:      1,	Adjusted R-squared:      1 
F-statistic: 1.182e+07 on 2 and 997 DF,  p-value: < 2.2e-16

> #----------------------------------------------------------------
> # OMITTED VARIABLE RESULTS
> summary(fit_omitted)

Call:
lm(formula = y ~ x1, data = data)

Coefficients:
            Estimate Std. Error t value Pr(>|t|)    
(Intercept)  2.93910    4.86159   0.605    0.546    
x1          -0.51169    0.08526  -6.001 2.74e-09 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 153.6 on 998 degrees of freedom
Multiple R-squared:  0.03483,	Adjusted R-squared:  0.03386 
F-statistic: 36.02 on 1 and 998 DF,  p-value: 2.736e-09
```

## Recap

In the simulation, omitting $$x_2$$ will cause the point estimates for $$x_1$$ to change from (positive) $$0.999$$ with a p-value of nearly zero, to (negative!) $$-0.512$$, also with a p-value of nearly zero! 

More generally, this reinforces the mantra that unless very specific assumptions are met, regression results should only be taken as linear predictors of an outcome, and not as a cause and effect relationship. Further, you cannot rely on statistical significance to guide you about whether your model is "well specified" or not. 
