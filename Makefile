setup:
	pip install -r requirements.pip

migrations:
	python manage.py makemigrations campeonatos

migrate: 
	python manage.py migrate

superuser:
	python manage.py createsuperuser

shell:
	python manage.py shell

run:
	python manage.py runserver 