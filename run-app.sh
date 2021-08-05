#!bin/bash

# RUN SERVICES
/usr/bin/docker-compose up -d

# EXECUTE MIGRATIONS
/usr/bin/docker-compose exec rest-srv python3 manage.py migrate --noinput

