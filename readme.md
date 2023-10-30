# mailing_service_coursework

What does this project do.
the program is a micro-service with a web interface. designed to organize mailings via email with separation of rights. writen by kirill.s (aka Mk.K) 2023. Python rulez! =)

How to prepare.
Be sure that you are going use it under linux-compatible operation system. this program use next external components: - cron - postgresql database - redis-server - sending emails through smtp protocol
How to install.
- clone project to own disk in new directory - activate virtual environment (python -m venv venv) - install all needs packages (pip install -r requirements.txt) - see next step for configure
How to configure.
Please pay your attention to configure .env file you can find example in root of your project directory please fill all parameters with your data and save the changed file as .env
after that you need create empty database you may use command

psql -U postgres

and then

CREATE DATABASE <database_name>

alternatively you can use pgadmin or other interface app. use next commands for tables creation

python manage.py migrate

and next for create default users

python manage.py create_default_group

Ноw it works.
RUN, Forest, RUN! Start the server with >python manage.py runserver
you will find web interface of the service on http://127.0.0.1:8000/ use it with any browser what you like.