release: python manage.py migrate
web: python inject_secrets.py && gunicorn "medmate.wsgi"