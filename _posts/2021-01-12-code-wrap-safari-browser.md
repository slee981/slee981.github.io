---
title: Text Wraps in Safari, but Scrolls in Chrome
layout: post
author: Stephen Lee 

toc: true
categories: [web development, front end]
tags: [css, html]
---

## Problem
On your website, you want to display text (like code) that should not wrap to a new line if it exceeds its y-axis boundary. In other words, if a line of text is too long, you want the option to scroll, as in the screenshot below: 

<div class="row py-3">
    <div class="col d-flex justify-content-center">
        <img class="small-img" alt="" src="{{ 'assets/images/code_wrap/code-with-scroll.png' | relative_url }}">
    </div>
</div>

However, in several different contexts I've noticed that what works in Brave and Chrome doesn't necessarily work in Safari. 

## Solution 

I've recreated a minimum working example to emphasize this point. 

Imagine you write the following HTML / CSS code: 

```html
<html>
<style>
code {
    width: 250px;
    background-color: lightgrey;
    display: block;
    overflow: auto;
    word-wrap: break-word;
}

.i-1 {
    padding: 0 1rem;
}
</style>

<body>
    <div class="code-block">
        <pre>
            <code>
                <span>def main():</span>
                <span class="i-1">my_really_long_var_name = [11, 32, 5, 53, 23, 67, 46, 7, 34, 2]</span>
            </code>
        </pre>
    </div>
</body>
</html>
```

This will produce the following output in Brave browser (I assume it's the same for Chrome). 

<div class="row py-3">
    <div class="col d-flex justify-content-center">
        <img class="small-img" src="{{ 'assets/images/code_wrap/brave.png' | relative_url}}">
    </div>
</div>

However, it will produce the following results in Safari: 

<div class="row py-3">
    <div class="col d-flex justify-content-center">
        <img class="small-img" src="{{ 'assets/images/code_wrap/safari.png' | relative_url}}">
    </div>
</div>

Obviously, when there is such little code, it's obvious that the issue is with the line `word-wrap: break-word`. In other words, if we change the style to 

```git
- word-wrap: break-word;
+ word-wrap: normal;
```

then it works in both browsers. But when it's late, and you're staring at this screen

<div class="row py-3">
    <div class="col d-flex justify-content-center">
        <img src="{{ 'assets/images/code_wrap/safari-dev.png' | relative_url}}">
    </div>
</div>

let's just say that things can take longer than you hope. 

## Summary

Safari and Brave / Chrome handle `word-wrap: break-word` differently when combined with `overflow: auto`. Brave and Chrome will still enforce the `overflow: auto`, while Safari will enforce the `word-wrap: break-word`. This can lead to confusion when using large and inherited style sheets. 

If you want your overflow code to scroll and not wrap in Safari browser, make sure your final `code` block settings look like this: 

```css
code {
    width: 250px;
    background-color: lightgrey;
    display: block;
    overflow: auto;
    word-wrap: normal;

    /*  
    ** TLDR: this works in brave, but not in safar
    **
    ** word-wrap: break-word; 
    */
}
```
