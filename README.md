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

$ python manage.py startapp <app>   # app is function
```

## Database Migration
```
$ python manage.py  makemigrations [app]

$ python manage.py migrate [app]
```

## Run
```
$ python manage.py runserver               # default run in 8000 port

$ python manage.py runserver 8080          # run in the port you want

$ ipconfig

$ python manage.py runserver 0.0.0.0:8000  # if you set the internal ip in ALLOWED_HOSTS of setting
```

## IDE (PyCharm) Setup
File > Setting > Project > Project Interpreter > Show All > Add > Existing environment > Interpreter > [Env]/Scripts/python.exe

## Package Requirement
- django
- diangorestframework
- pygments (code highlighting [this tutorial require])
