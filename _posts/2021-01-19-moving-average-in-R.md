---
title: Moving Average in R, tidyverse
author: Stephen Lee
layout: post

categories: [statistics, tutorial]
tags: [R, tidyverse, stats]
toc: true
katex: true
---

## Problem  

Given some dataset, you might want to find the rolling or moving average. We can visualize this in a sample dataset as follows. Note, the `k-lag` moving average we want, `MA-k`, is the mean of the last `k` observations in time, including the current one.  

```r 
# A tibble: 48 x 5
   Manufacturer  Date       Price  MA_3  MA_4
   <chr>         <date>     <dbl> <dbl> <dbl>
 1 A1 Industries 2010-03-31     5 NA    NA   
 2 A1 Industries 2010-06-30     4 NA    NA   
 3 A1 Industries 2010-09-30     3  4    NA   
 4 A1 Industries 2010-12-31     6  4.33  4.5 
 5 A1 Industries 2011-03-31     7  5.33  5   
 6 A1 Industries 2011-06-30     5  6     5.25
 7 A1 Industries 2011-09-30     4  5.33  5.5 
 8 A1 Industries 2011-12-31     4  4.33  5   
 9 A1 Industries 2012-03-31     5  4.33  4.5 
10 A1 Industries 2012-06-30     4  4.33  4.25
# … with 38 more rows
```

Additionally, however, we want to use `tidyverse` methodology: so no `for` loops. 

### Sample Data

For this post, I use a constructed dataset to emphasize the usecase I want. Namely, imagine we have a panel dataset of manufacturer prices over time, and we want to see how those prices change from a moving average perspective. 

The following code will generate a simulation dataset.

```r 
library(tidyverse)

data <- tibble(
    Manufacturer = c(
        rep("A1 Industries", 16),
        rep("B2 Factories", 16),
        rep("C3 Potentials", 16)
    ),
    Date = rep(
        as.Date(c(
            "2010-03-31", "2010-06-30", "2010-09-30", "2010-12-31",
            "2011-03-31", "2011-06-30", "2011-09-30", "2011-12-31",
            "2012-03-31", "2012-06-30", "2012-09-30", "2012-12-31",
            "2013-03-31", "2013-06-30", "2013-09-30", "2013-12-31"
        )), 3
    ),
    Price = rep(c(
        5, 4, 3, 6,
        7, 5, 4, 4
        ), 6
    )
)

# > data 
# # A tibble: 48 x 3
#    Manufacturer  Date       Price
#    <chr>         <date>     <dbl>
#  1 A1 Industries 2010-03-31     5
#  2 A1 Industries 2010-06-30     4
#  3 A1 Industries 2010-09-30     3
#  4 A1 Industries 2010-12-31     6
#  5 A1 Industries 2011-03-31     7
#  6 A1 Industries 2011-06-30     5
#  7 A1 Industries 2011-09-30     4
#  8 A1 Industries 2011-12-31     4
#  9 A1 Industries 2012-03-31     5
# 10 A1 Industries 2012-06-30     4
# # … with 38 more rows
```

### Setup

We can take advantage of an existing function in the `zoo` package, called `zoo::rollmean`, and modify it to fit this use case. 

On its own, `zoo::rollmean` exhibits the following behavior: 
```r
data %>%
    arrange(Manufacturer, Date) %>%
    group_by(Manufacturer) %>%
    mutate(
        Roll_3 = zoo::rollmean(Price, 3, fill = NA),
        Roll_4 = zoo::rollmean(Price, 3, fill = NA)
    ) %>%
    ungroup()

# # A tibble: 48 x 5
#    Manufacturer  Date       Price Roll_3 Roll_4
#    <chr>         <date>     <dbl>  <dbl>  <dbl>
#  1 A1 Industries 2010-03-31     5  NA     NA   
#  2 A1 Industries 2010-06-30     4   4      4   
#  3 A1 Industries 2010-09-30     3   4.33   4.33
#  4 A1 Industries 2010-12-31     6   5.33   5.33
#  5 A1 Industries 2011-03-31     7   6      6   
#  6 A1 Industries 2011-06-30     5   5.33   5.33
#  7 A1 Industries 2011-09-30     4   4.33   4.33
#  8 A1 Industries 2011-12-31     4   4.33   4.33
#  9 A1 Industries 2012-03-31     5   4.33   4.33
# 10 A1 Industries 2012-06-30     4   4      4   
# # … with 38 more rows
```

Not what I expected! In this case, the default behavior is to take the rolling mean *centered* on the given row, meaning it is using fututre "lead" data, as well as past "lagged" data. Note the use of `fill = NA`. this just tells the function how to pad the data, since any use of lagged variabes will necessarily shrink the number of usable rows. 

There are some other options that sound promising, but they do not seem to work for me. 

```r
data %>%
    arrange(Manufacturer, Date) %>%
    group_by(Manufacturer) %>%
    mutate(
        Roll_4_right = zoo::rollmean(Price, 3, fill = NA, align = "right"),
        Roll_4_left = zoo::rollmean(Price, 3, fill = NA, align = "left")
    ) %>%
    ungroup()

# # A tibble: 48 x 5
#    Manufacturer  Date       Price Roll_4_right Roll_4_left
#    <chr>         <date>     <dbl>        <dbl>       <dbl>
#  1 A1 Industries 2010-03-31     5        NA           4   
#  2 A1 Industries 2010-06-30     4        NA           4.33
#  3 A1 Industries 2010-09-30     3         4           5.33
#  4 A1 Industries 2010-12-31     6         4.33        6   
#  5 A1 Industries 2011-03-31     7         5.33        5.33
#  6 A1 Industries 2011-06-30     5         6           4.33
#  7 A1 Industries 2011-09-30     4         5.33        4.33
#  8 A1 Industries 2011-12-31     4         4.33        4.33
#  9 A1 Industries 2012-03-31     5         4.33        4   
# 10 A1 Industries 2012-06-30     4         4.33        4.33
# # … with 38 more rows
```

## Solution 

In this case, the behavior is mostly correct, so I wrap this function to give it the behavior I want. 

```r
moving_average <- function(series, klags) {
    return(
        lag(
            zoo::rollmean(series, klags, fill = NA), floor(klags / 2)
        )
    )
}
```

This will first calculate the rolling mean with the `zoo` package function, and then shift the results back to where we want them. The use of `floor(klags / 2)` accounts for how `zoo::rollmean` handles even and odd numbers. 

The result is the following: 

```r
ma_data <- data %>%
    arrange(Manufacturer, Date) %>%
    group_by(Manufacturer) %>%
    mutate(
        MA_3 = moving_average(Price, 3),
        MA_4 = moving_average(Price, 4),
        MA_5 = moving_average(Price, 5),
        MA_6 = moving_average(Price, 6),
    ) %>%
    ungroup()

# > ma_data 
# # A tibble: 48 x 7
#    Manufacturer  Date       Price  MA_3  MA_4  MA_5  MA_6
#    <chr>         <date>     <dbl> <dbl> <dbl> <dbl> <dbl>
#  1 A1 Industries 2010-03-31     5 NA    NA     NA   NA   
#  2 A1 Industries 2010-06-30     4 NA    NA     NA   NA   
#  3 A1 Industries 2010-09-30     3  4    NA     NA   NA   
#  4 A1 Industries 2010-12-31     6  4.33  4.5   NA   NA   
#  5 A1 Industries 2011-03-31     7  5.33  5      5   NA   
#  6 A1 Industries 2011-06-30     5  6     5.25   5    5   
#  7 A1 Industries 2011-09-30     4  5.33  5.5    5    4.83
#  8 A1 Industries 2011-12-31     4  4.33  5      5.2  4.83
#  9 A1 Industries 2012-03-31     5  4.33  4.5    5    5.17
# 10 A1 Industries 2012-06-30     4  4.33  4.25   4.4  4.83
# # … with 38 more rows
```

To convince yourself that this works on the different groups e.g. manufacturers, view this table in R Studio 

```r 
View(ma_data)
```



