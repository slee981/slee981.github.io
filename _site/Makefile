start: 
	bundle
	bundle exec jekyll serve

build-and-publish: build 
	$(MAKE) publish

publish: 
	git subtree push --prefix _site origin gh-pages

build: 
	bundle 
	JEKYLL_ENV=production bundle exec jekyll build