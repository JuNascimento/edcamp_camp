setup:
	pip install -r requirements.pip

create-db:
	mysql -uroot -e "create database if not exists edcamp_camp" ;

migrations:
	python manage.py makemigrations campeonatos

migrate: migrations
	python manage.py migrate

superuser:
	python manage.py createsuperuser

shell:
	python manage.py shell


run:
	python manage.py runserver 