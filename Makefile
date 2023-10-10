format:
	black .

lint:
	flake8 .


shell:
	python manage.py shell_plus

tests:
	python manage.py test -v 2 --keepdb

