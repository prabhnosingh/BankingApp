# banking application

To install dependencies run:
1.  git clone -b dev <url git repo>
2.  pip install -r requirements.txt
3.  delete the migration files if you got them while cloning
4.  python manage.py make migrations
5.  python manage.py migrate
6.  python manage.py runserver
7.  python manage.py createsuperuser
