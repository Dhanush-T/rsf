#!/bin/sh

until psql postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${SQL_HOST}/${POSTGRES_DB} -c '\l'; do
    echo -e "\e[34m >>> Postgres is unavailable - sleeping \e[97m"
    sleep 1
done

python manage.py makemigrations --settings=rsf.settings.production
python manage.py migrate --settings=rsf.settings.production
python manage.py create_admin --settings=rsf.settings.production
python manage.py collectstatic --settings=rsf.settings.production --no-input --clear
python manage.py update_index --settings=rsf.settings.production
exec "$@"
