pip install -r requirements.txt
python manage.py migrate
python manage.py createcachetable
python manage.py load_initial_data
python manage.py collectstatic --noinput
python manage.py runserver
pause