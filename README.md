# djangotemplateproject

## Introduction

Django can be a very useful framework. 

- Django simplifies database operations. There is no overhead implementation.
  - Tables are implemented in "models.py".  
  - Data read and write operations are done with one line of code.
- Django simplifies url management.
- For UI implementation, it has a template language.

However, to prepare the system for the first time, there are lots of things to do.
- Configure settings.py
  - allauth django application for login system
  - database settings; database engine, database name, user name, user password, host, port
  - static files folder path
- Configure urls.py; admin urls, application urls, login urls
- Download javascript libraries
- Implementing index page; html file, url mapping, view url directing

___

## Prerequisites
- Docker

## Preprocessing

- Set project and application name
```bash
python ./setup/rename/renameProjectAndApplication.py project_name application_name
```

## Installation
