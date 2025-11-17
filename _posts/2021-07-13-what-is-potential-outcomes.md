---
title: What is the "Potential Outcomes" Framework
author: Stephen Lee
layout: post

categories: ["Potential Outcomes"]
tags: ["Potential Outcomes"]
toc: true
katex: true
---

## Overview
Potential outcomes is a set of techniques and tools for estimating the likely results of a particular action. More specifically, potential outcomes provides a methodology for assessing the effect of a treatment (aka intervention) when certain assumptions are believed to be true. Notably, this approach is often applied to observational data in fields like economics, epidemiology, or sociology, where many experiments would be prohibitedly expensive or unethical. 

While the randomized control trial is often considered a benchmark for causal inference,[^1] practitioners of potential outcomes argue that these methods can be naturally applied to other settings as well. Intuitively, the belief is that since we humans seem able to draw useful inference about the world without rigorous experiment (e.g. taking an asprine will help my headache because it helped last time), formalizing the process of observational based inference can yield valuable insight. 

## Philosophy 
One way to think about cause and effect is as a comparison between outcomes: what would be the difference in my outcome if I receive the treatment, compared to if I do not receive the treatment? In other words, what is the difference between the *potential outcomes*? Central to this is the missing data problem, also referred to as the fundamental problem of causal inference. In short, (for a given unit): 

> You can only either observe the outcome after treatment, or after no-treatment. 
> 
> Since we cannot go back in time, we cannot observe both, and hence, we cannot measure true effects at an individual level of analysis. 

The workaround for potential outcomes is to focus on treatment groups to estimate aggregated effects, as opposed to individual level effects. For example, we may measure the average treatment effect (ATE) or the 25th percentile treatement effect, but we cannot measure Bob or Ann's specific treatment effect. 

Note, there is another popular approach to thinking through causal inference problems often referred to as structural modeling. For example, the Structural Causal Model (SCM) popularized by Judea Pearl requires statement of all relevant variables, and their potential interactions. In his words, one must specify, "who talks to whom". With this, one can then utilize graphical abstractions of these relationships in the form of directed acyclic graphs (DAGs), and follow certain proceedural rules to discover if your causal question can be estimated with the data you have i.e. are you missing observation of any variables that are critical to the estimation. Beyond this, there is a long tradition of structural economic modeling, and in particular with simultaneously determined relationships like supply and demand. This will likely become a separate blog post, but for now, this is outside the scope of this post.

## Assumptions

> Causal conclusions are only as valid as the causal assumptions upon which they rest.
>
> -- Judea Pearl

What makes assumptions so tricky is that in many cases you cannot test them for validity. For an analysis of potential outcomes, two main categories of assumptions are needed:

### (1) Stable Unit Treatment Value Assumption (SUTVA)
According to Donald Rubin (who is largely credited with shaping this literature), this assumption requires: 
1. There are no individual spillovers (i.e. no externalities).
1. There is no hidden variation in the treatment e.g. strength or adherence.

For example, if studying the effect of graded homework on student performance at a university, there could likely be spillovers in the form of peer effects: a "treatment" classroom may impact student performance in a "control" classroom if friends from both groups study together. 

Further, this assumption also requires only one "strength" of treatment. To extend the same example, if the treatment is to assign graded homeworks, compared to a control where students do not have their homework assignments graded, each classroom in the treatment group must grade homework assignments with the same frequency. In other words, if one teacher in the treatment group returns graded assignments every week, while another teacher in the treatment group only returns graded assignments once a month, the final causal inference would likely be conflated.

When these conditions are met, the causal analysis is greatly simplified. Unfortunately however, these are rather strong assumptions and often may not be plausible. Fortunately, there is a growing body of research to best handle estimation when these assumptions are relaxed. 

### (2) Assignment Mechanism
When comparing a group that received treatment to a group that didn't receive treatment, we need to know (or make an assumption) about why certain individuals were assigned to the treatment group, while others were not. 

In the simplest case, this assignment is random (as in a clinical trial) and unconfounded insofar as assignment does not depend on the potential outcomes. In other words, if all of the individuals that received treatment were given it precicely because they had the most to benefit, a straight forward comparison between the outcomes of the treatment and control groups woudl not represent a causal effect of the treatment. 

For example, one may wonder what is the causal effect of attending and graduating from a university. Since it would be unethical, costly, and infeasible in a reasonable timeline, we do not perform this experiment. Thus, we may try to use observational data on students that graduated from university and compare their outcomes to students that didn't attend. In this case, the causal inference is complicated by the fact that the decision to attend or not attend college is likely incluenced by the perceived benefit of attending. Thus, the treatment (attend college) may depend on the potential outcome (do you expect to be better or worse off if you attend?). 

Various tools have been developed to handle cases where the assignment is not random or the distribution of the assignment is unknown. For these, techniques rapidly become more and more sophisticated, and assumptions become more and more layered. Overall, estimation can still occur, but it's much more difficult.  

## Resources 
- *Causal Inference for Statistics, Social, and Biomedical Sciences*. Imbens G. and Rubin D. 
- *Causal Inference: The Mixtape*. Cunningham S. 

## Footnotes

[^1]: Consider, as evidence, that this is the requirement for a drug to pass FDA inspection. 
[^2]: 