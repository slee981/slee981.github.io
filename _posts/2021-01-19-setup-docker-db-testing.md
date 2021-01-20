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

For these examples, I'm using Docker version 3.1.0 on OSX. 

### Example 1: DB only 
For this, I'm using MySQL, although conceptually changing to any other database (e.g. PostGREs, Mongo, Maria) is straightforward. To create a Docker managed database (without a corresponding database management system), we can create the following `Makefile`.

#### Setup
```makefile
# ./Makefile 

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
start-db:
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

clean:
	docker volume rm $(MYSQL_DATA_IMAGE_NAME)
```

And, we can provide the specified environment configuration file as follows: 

```list
# ./dev.mysql.list

MYSQL_USER=steve
MYSQL_PASSWORD=password
MYSQL_ROOT_PASSWORD=password
```

#### Run 
To run this, `cd` into the same directory as the `Makefile`, and enter: 
```bash 
$ ls
Makefile    dev.mysql.list

$ make setup
$ make start-db
```

You can then interact with the database via the cli. For example, to administer user permissions (for later use when seeding data, or whatever), you might do the following.
```bash 
$ make shell-root
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 2
Server version: 5.7.32 MySQL Community Server (GPL)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.01 sec)

mysql> SHOW GRANTS for 'steve'; 
+------------------------------------------------------+
| Grants for steve@%                                |
+------------------------------------------------------+
| GRANT USAGE ON *.* TO 'steve'@'%'                |
+------------------------------------------------------+
1 rows in set (0.00 sec)

mysql> GRANT INSERT, UPDATE, DELETE ON *.* TO 'steve';
Query OK, 0 rows affected (0.00 sec)

mysql> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.00 sec)

mysql> SHOW GRANTS FOR 'steve';
+----------------------------------------------------+
| Grants for steve@%                                 |
+----------------------------------------------------+
| GRANT SELECT, INSERT, UPDATE ON *.* TO 'steve'@'%' |
+----------------------------------------------------+
1 row in set (0.00 sec)
```

And later, to stop the database container, run
```bash 
$ make stop
```

And finally, if you want to destroy the data from that database to free up hard drive space, type
```bash 
$ make clean
```

### Example 2: DB and DBMS
Sometimes you may additionally want to have available a database management system without committing to a full install. For example, Sequel Ace is a very popular piece of database management software for MySQL and Maria databases, but is only compatible on OSX. MySQL Workbench is a popular but bulky choice if you're not 100% committed to using it regularly.     

In this case, we can use `docker-compose` to build both the database server, and a locally hosted database management system. 

#### Setup 
We'll again use MySQL as the database, and select Adminer (formerly phpMyAdmin) as the database management system. It's not *amazing*, but it does everything we need as lightweight solution. 

First, create a `docker-compose.yml` file

```yml
# ./docker-compose.yml

version: '3.1'

services:

  adminer:
    container_name: admin_portal
    image: adminer
    restart: always
    ports:
      - 8080:8080

  db:
    container_name: steve_db
    image: mysql:5.6
    ports: 
      - 3306:3306
    volumes: 
      - steve_data:/var/lib/mysql
    env_file: 
      - mysql.dev.list
      
volumes: 
  steve_data:
```

The mysql environment configuation file, `mysql.dev.list`
```
# ./mysql.dev.list

MYSQL_ROOT_PASSWORD=password
MYSQL_USER=steve
MYSQL_PASSWORD=password
MYSQL_DATABASE=test_db
```

Finally, we can build a `Makefile` to simplify commands 

```makefile 
# ./Makefile

DATABASE_IMAGE=steve_db
DEFAULT_USER=steve

up: 
	docker-compose up -d

down: 
	docker-compose down

shell: 
	docker exec -it $(DATABASE_CONTAINER) mysql -u $(DEFAULT_USER) -p 

inspect: 
	docker inspect $(DATABASE_CONTAINER)

ip_addr: 
	docker inspect $(DATABASE_CONTAINER) | grep IPAddress
```

#### Run
Now, to start the database, we `cd` into the root directory with the `Makefile` and `docker-compose.yml` and run 

```bash 
$ ls 
Makefile    docker-compose.yml    mysql.dev.list

$ make up 
```

Now, we can either interact with the database via the cli

```bash 
$ make shell
```

Or, we can open a browser, navigate to https://localhost:8080, and find Adminer. Simply login with the credentials you provided in the `mysql.dev.list` configuration file. 



