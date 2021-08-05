Yahoo Scrapping App
===================

\

If you want to search throw all articles go to [LINK](/news/)

If you want to get all articles throw API use
[LINK](/news/api/?type=AAPL)

* * * * *

Run app steps:
==============

1.  **docker-compose up -d** - create containers and run
2.  **docker-compose exec rest-srv python3 manage.py migrate --noinput**
    - run database migrations
3.  **docker-compose exec rest-srv python3 manage.py createsuperuser
    --username=user1 --email=user1@example.com** - create super user so
    user can create cronjob in admin panel
4.  **docker-compose exec rest-srv celery -A yahoo\_scrapper worker
    --beat --loglevel=info** - start celary scheduled jobs

* * * * *

### Project structure - apps

-   **yahoo\_scrapper** --- main app
-   **get\_news** --- app for scrapping urls and storing articles into
    database
-   **serve\_news** --- app for getting articles from database and
    displaying on /news/ route

* * * * *

### Developed on Linux Mint

* * * * *

### Packages used:

-   pip install redis
-   pip install celery
-   pip install django-celery-beat (python manage.py migrate
    django\_celery\_beat)
-   pip install feedparser
-   pip install psycopg2

### Linux Mint installs

-   sudo apt-get install python3-pip python3-dev libpq-dev postgresql
    postgresql-contrib
-   sudo apt-get install python-dev libpq-dev postgresql
    postgresql-contrib
-   sudo apt install redis-server

### check celer jobs

celery -A yahoo\_scrapper worker -l info

### starting scrapper cronjobs

celery -A yahoo\_scrapper worker --beat --loglevel=info
