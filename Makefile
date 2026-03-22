init: setup start

setup:
	pip install -r requirements.txt
	python manage.py migrate
	python manage.py createcachetable
	python manage.py load_initial_data
	python manage.py collectstatic --noinput

start:
	python manage.py runserver

reset-db:
	del db.sqlite3
	python manage.py migrate
	python manage.py createcachetable
	python manage.py load_initial_data