# ATTENTION THIS README IS ONLY FOR DEVELOPERS PLEASE USE A DIFFERENT ONE FOR PUBLIC
# PrismLoad
A cryptocurrency made for online shopping

Here a quick start guide to build the source

===[Written by Rían Ó Donnell]=====

Get MySQL


## Getting Started
To get started download the folder



When you have downloaded, cd into the source folder and run app.py
```
cd C:/Downloads/prismload/ (probably different for you)
 python application.py
```
Its now up and running!

## Prerequisites

### Install mySQL
Note: You may skip this if you already have mySQL installed
```
$ brew install mysql 
$ brew tap homebrew/services
$ brew services start mysql
$ mysqladmin -u root password 'yourpassword' 
```

### Configure mySQL 
Start mySql session in terminal
```$ mysql -u root -p```

#### Create database and tables
``` 
mysql> 
       CREATE DATABASE shockwave;
       use shockwave;
       CREATE TABLE users(name varchar(30), email varchar(30), username varchar(20), password varchar(50));
       CREATE TABLE blockchain(number varchar(30), hash varchar(68), previous varchar(68), data varchar(100), nonce varchar(30));
```

#### Configure Database Config File
Update Line 41 in ```app.py``` with the password saved above



### Dependencies
Make sure you have Python 3 installed. Install the following dependencies.


```  


$ pip install Flask
  pip install simple-crypt
  pip install passlib
  pip install flask_mysqldb #mySql must be installed, see below
  pip install functools
  pip install wtforms
```






