# djrst
for learning django rest framework

```
django-admin startproject project_name
cd project project_name
python3 manage.py startapp app_name
python3 manage.py migrate
python3 manage.py makemigrations #db
python3 manage.py runserver

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# Media Files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

./manage.py collectstatic
```
