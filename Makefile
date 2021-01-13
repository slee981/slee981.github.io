start: 
	bundle
	bundle exec jekyll serve

build-and-publish: build 
	$(shell git add .)
	$(shell git commit -m "update build")
	publish

publish: 
	# this repo runs from master
	# git subtree push --prefix _site origin gh-pages
	git push 

build: 
	bundle 
	JEKYLL_ENV=production bundle exec jekyll build