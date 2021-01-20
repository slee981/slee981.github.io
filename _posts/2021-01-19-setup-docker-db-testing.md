---
title: Use Docker for Local Databases 
layout: post
author: Stephen Lee 

toc: true
categories: [database, backend]
tags: [docker, mysql]
---

## Problem 

You want access to a local database for some reason. You might be doing web or app development, or practicing SQL queries, or whatever. Why you want a local database is your business. 

## Solution 

Use Docker. It can manage your data (with `docker volume`), your databases and versions (with `docker images`), and makes cleanup very simple so as to not overburden your computer. 

### Example 1: DB only 
For this, I'm using MySQL, although conceptually changing to any other database (e.g. PostGREs, Mongo, Maria) is straightforward. To create a Docker managed database (without a corresponding database management system), we can create the following `Makefile`.

#### Setup
```makefile
# local variables 
# these can be imported from a separate config file 
MYSQL_DATA_IMAGE_NAME=steve-data
MYSQL_INIT_FILE=dev.mysql.list
SHELL_USER=steve

DOCKER_NETWORK=steve-network
MYSQL_IMAGE_NAME=steve-dev-mysql
MYSQL_PORT=3306 # <-- can be different to avoid port collisions.

# create network and volume
# only needs to be run once
setup:
	docker network create $(DOCKER_NETWORK)
	docker volume create --name $(MYSQL_DATA_IMAGE_NAME)

# start database in a docker instance.
start-db: stop-db
	docker run --name $(MYSQL_IMAGE_NAME) -v $(MYSQL_DATA_IMAGE_NAME):/var/lib/mysql --network $(DOCKER_NETWORK) --env-file $(MYSQL_INIT_FILE) --detach --publish $(MYSQL_PORT):3306 mysql:5.7

# stop database instance.
stop-db:
	docker stop $(MYSQL_IMAGE_NAME)
	docker rm $(MYSQL_IMAGE_NAME)

shell: 
	docker exec -it $(MYSQL_IMAGE_NAME) mysql -u $(SHELL_USER) -p 

shell-root: 
	docker exec -it $(MYSQL_IMAGE_NAME) mysql -u root -p 

inspect: 
	docker inspect $(MYSQL_IMAGE_NAME)

ip_addr: 
	docker inspect $(MYSQL_IMAGE_NAME) | grep IPAddress
```

And, we can provide the specified environment configuration file as follows: 

```list
MYSQL_USER=steve
MYSQL_PASSWORD=password
MYSQL_ROOT_PASSWORD=password
```

#### Run 

### Example 2: DB and DBMS

#### Setup 

#### Run



