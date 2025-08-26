App2 - scaffolded app

Files added:
- views.py, urls.py, models.py, admin.py
- templates/app2/index.html and detail.html
- static/app2/style.css
- migrations/__init__.py

Next steps:
1. Add 'app2' to INSTALLED_APPS in project `settings.py`.
2. Include the app urls in your project `urls.py` e.g. `path("", include("app2.urls"))`.
3. Run `python manage.py makemigrations app2` and `python manage.py migrate`.
4. Create a superuser to access admin: `python manage.py createsuperuser`.
