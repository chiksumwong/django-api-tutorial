# Django Tutorial

## Setup Environment
```
$ pip install virtualenv

$ cd <Project Folder>

$ virtualenv <env>
```

## Active / Inactive Env
```
$ cd <env>

$ scripts\activate

$ deactivate
```

## Setup Project
```
$ django-admin startproject <project>

$ cd [project]

$ python manage.py startapp <app>
```

## Database Migration
```
$ python manage.py  makemigrations [app]

$ python manage.py migrate [app]
```

## Run
```
$ python manage.py runserver
```

## IDE (PyCharm) Setup
File > Setting > Project > Project Interpreter > Show All > Add > Existing environment > Interpreter > [Env]/Scripts/python.exe

## Package Requirement
- django
- diangorestframework
- pygments (code highlighting [this tutorial require])
