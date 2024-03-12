# banking application

To install dependencies run:
1.  git clone -b dev <url git repo>
2.  pip install -r requirements.txt
3.  delete the migration files if you got them while cloning
4.  pip install shortuuid
5.  pip install django-import-export
6.  python -m pip install Pillow
7.  python manage.py make migrations
8.  python manage.py migrate
9.  python manage.py runserver
10.  python manage.py createsuperuser

