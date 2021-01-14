---
title: Deploy Jekyll to GitHub Pages
layout: post
author: Stephen Lee 

toc: true
categories: [web development, front end]
tags: [jekyll, git, github]
---

## Problem 
You have made a beautiful blog with Jekyll (and hopefully with the [Cadre theme](https://github.com/slee981/jekyll-theme-cadre)), but don't know the best workflow to make it go live on the Internet. 

## Solution 
There are two options depending on your use case and preferences. 

### Using the `github-pages` plugin
When you create a new Jekyll project, the boilerplate `Gemfile` has the following lines: 

```bash
# ./ Gemfile

source "https://rubygems.org"
# Hello! This is where you manage which Jekyll version is used to run.
# When you want to use a different version, change it below, save the
# file and run `bundle install`. Run Jekyll with `bundle exec`, like so: # #     bundle exec jekyll serve
#
# This will help ensure the proper Jekyll version is running.
# Happy Jekylling!
gem "jekyll", "~> 4.2.0"
# This is the default theme for new Jekyll sites. You may change this to anything you like.
# gem "minima", "~> 2.5"
gem "jekyll-theme-cadre", "~> 0.1.20"
# If you want to use GitHub Pages, remove the "gem "jekyll"" above and
# uncomment the line below. To upgrade, run `bundle update github-pages`.
# gem "github-pages", group: :jekyll_plugins

# ...
```

If you want to use another theme, you change that here. Similarily, as the comments suggest, you comment out the `jekyll` line and uncomment the `github-pages` line. Your ready-to-deploy `Gemfile` might look like this: 

#### `Gemfile` and `_config.yml`
```bash
# ./ Gemfile

source "https://rubygems.org"
# Hello! This is where you manage which Jekyll version is used to run.
# When you want to use a different version, change it below, save the
# file and run `bundle install`. Run Jekyll with `bundle exec`, like so:
#
#     bundle exec jekyll serve
#
# This will help ensure the proper Jekyll version is running.
# Happy Jekylling!
# gem "jekyll", "~> 4.2.0"
# This is the default theme for new Jekyll sites. You may change this to anything you like.
# gem "minima", "~> 2.5"
gem "jekyll-theme-cadre", "~> 0.1.20"
# If you want to use GitHub Pages, remove the "gem "jekyll"" above and
# uncomment the line below. To upgrade, run `bundle update github-pages`.
gem "github-pages", group: :jekyll_plugins

# ...
```

For safety reasons, GitHub Pages does not support running "unapproved" themes. There is a workaround. In your `_config.yml` file, use 

```yml
# ./_config.yml

# url settings are important for finding 
# all the 'assets' like images and style sheets

# if using github
url: "ghuser.github.io"

# if on a project repository, 
# the exact name of that repo
baseurl: "repo-name"

# Build settings
plugins:
  - jekyll-feed
  - jekyll-remote-theme

# this will not work!
# theme: jekyll-theme-cadre
#
# use this instead!
remote_theme: slee981/jekyll-theme-cadre
```

#### Deploy
Now, you can push your repo as normal to a `gh-pages` branch. For example: 

```bash 
~/Documents/MyBlog (master) 
$ git checkout -b gh-pages

~/Documents/MyBlog (gh-pages) 
$ git push -u origin gh-pages 
```

After a few minutes, you should see your site live. If you want to deploy to a custom domain name, the GitHub Pages documentation is an excellent guide. 

### Build and push `_site` folder
One issue with the first approach is that the workflow for testing your site locally is a bit more complicated: 
1. You have to change the `Gemfile` to run locally with `bundle exec jekyll serve`. 
1. You have to add the additional `remote_theme` option for "unsupported themes, but I've not had luck getting that to work locally either. 

#### `Gemfile` and `_config.yml`
In this case, I use the standard `Gemfile` 

```bash 
# ./ Gemfile

source "https://rubygems.org"

gem "jekyll", "~> 4.2.0"
gem "jekyll-theme-cadre", "~> 0.1.20"
# ...
```

and the standard `_config.yml`
 
```yml
# ./_config.yml

theme: jekyll-theme-cadre

# Build settings
plugins:
  - jekyll-feed
```

This will build locally with: 

```bash 
$ bundle exec jekyll serve
```

Now I can work locally on a `dev` branch, and, without checking out a different branch, build the static `_site` folder and push it directly to the remote `gh-pages` branch. 

#### Deploy
First, we need to tell `git` to track the changes for the `_site` folder: 
```bash
# ./.gitignore

# _site    <-- comment this out or delete
.sass-cache
.jekyll-cache
.jekyll-metadata
vendor
```

```bash 
$ bundle 
$ # 
$ # build for production 
$ JEKYLL_ENV=production bundle exec jekyll build
$ # 
$ # commit the changes 
$ git add . 
$ git commit -m "update with build" 
$ # 
$ # push the "_site" subfolder 
$ git subtree push --prefix _site origin gh-pages
```

##### Add to Makefile
Skip the typing and add these shortcuts in a `Makefile`: 
```makefile
# ./Makefile

start: 
	bundle
	bundle exec jekyll serve

publish: 
	git subtree push --prefix _site origin gh-pages

build: 
	bundle 
	JEKYLL_ENV=production bundle exec jekyll build
```

Now, after editing a new post, updating the live site only requires: 

```bash 
$ make build 
$ git add .
$ git commit -m "add new post" 
$ git push 
$ make publish 
```
