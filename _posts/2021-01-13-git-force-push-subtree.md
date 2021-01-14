---
title: Force Push a Git Subtree
layout: post
author: Stephen Lee 

toc: true
categories: [version control]
tags: [git]
---

## Problem
For... reasons... you force pushed a branch to your remote repository. For example, I've definitely done the following thing before (not that I'm proud of it): 

```bash 
$ git add . 
$ git commit -m "useful message" 
$ git push 
$ #
$ # shoot, i really should have also changed [ ... ]
$ git add . 
$ git commit -m "..." 
$ #
$ # interactive rebase to "fixup" the last commit
$ # i.e. this essentially puts the last change into 
$ #      the previous commit message 
$ git rebase -i HEAD~2
$ git push -f
```

Additionally, if this repo is, for example, a Jekyll blog, you may be building the `_site` folder and pushing only that to the remote `gh-pages` branch. 

```bash 
git subtree push --prefix _site origin gh-pages
```

However, after you just did a dumb dumb thing and forced a push, the next time you run the `git subtree push ...` command, you will get a hard reject - something like this: 

```bash 
! [rejected]        gh-pages -> gh-pages (fetch first)
error: failed to push some refs to 'file:///...'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first merge the remote changes (e.g.,
hint: 'git pull') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

## Solution 

In this case, pulling will not help because it thinks you have less (and older) code than it does. You did just bury some changes into a previous commit message, after all. 

The following solution is taken shamelessly from [this excellent GitHub Gist](https://gist.github.com/tduarte/eac064b4778711b116bb827f8c9bef7b) and preserved here for others (including my future-self) to find. 

```bash 
$ # create a local gh-pages branch containing the splitted output folder
$ git subtree split --prefix _site -b gh-pages 
$ #
$ # force the push of the gh-pages branch to the remote gh-pages branch at origin
$ git push -f origin gh-pages:gh-pages 
$ #
$ # delete the local gh-pages because you will need it later
$ git branch -D gh-pages 
```

You are now free to go about your business.
