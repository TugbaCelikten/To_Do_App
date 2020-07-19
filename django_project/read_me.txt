
pip  install virtualenv 
virtualenv djangoenv
activate.bat
pip install django

python manage.py runserver


Admin bolumu

1. python manage.py migrate
2. python manage.py createsuperuser (admin user)
3. python manage.py startapp todo_app

