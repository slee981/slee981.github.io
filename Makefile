start: 
	bundle
	bundle exec jekyll serve

build-and-deploy: build 
	$(shell git add .)
	$(shell git commit -m "update build")
	deploy

deploy: 
	git subtree push --prefix _site origin gh-pages

build: 
	bundle 
	bundle exec jekyll build