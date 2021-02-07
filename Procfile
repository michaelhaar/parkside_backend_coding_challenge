release: cd django_webserver && python3 manage.py migrate
web: cd django_webserver && gunicorn config.wsgi --preload --log-file -