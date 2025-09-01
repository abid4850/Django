# DJANGO

## Installation

### miniconda
```bash
conda create -n django python=3.11 -y
conda activate django
pip install django
```

### python env
```bash
python -m venv .venv
source .venv/bin/activate # for Linux/Mac
.venv\Scripts\activate # for Windows
pip install django
```

## Create a Django project
```bash
django-admin startproject codanics # codanics is the project name
cd codanics
python manage.py runserver
# python manage.py runserver 8001
```
## 4. Create an app 

Apps in django are modular components that encapsulate specific funtionality.
They can be reused across different projects.



'''bash 
python manage.py startapp cources

