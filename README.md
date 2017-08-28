# duka-connect

## Soft drinks survey

#### Local setup
__This is a guideline to run the app locally__
```bash
mkdir app
cd app
virtualenv -p /usr/bin/python2.7 .
git clone https://github.com/johngathure/duka-connect.git
. bin/activate
cd duka-connect
pip install -r requirements.txt

# run tests
./manage.py test --settings=dukaconnect.test_settings

# change the env file database configurations ie host, name, user and password then save.
./manage.py migrate
./manage.py loaddata drink.json
# create a super user for the dashboard
./manage.py createsuperuser
./manage.py runserver
```
__To view the api docs run the following__

Serving the docs runs on port 8000, If the django app is running on that port too,
you might have to stop it then run the on a diffrent port.
```bash
cd docs
mkdocs serve
```

The admin dashboard can be viewed at
http://localhost:8000/admin

### Docker deployment
__Requirements.__
The server must have the following installed.

1. Docker
2. Docker compose

If you haven't, visit https://www.docker.com/  for guidelines

- log in into your server
- clone the source to any location of your choice.
- Configure the env file to contain the correct information, ie database host, user, name, and password.
  Host should be "database", the name of the postgres container defined in the docker-compose.yml file
  Also set debug to false.
- Run docker-compose up

On a successfull run of the docker-compse up command, type docker ps
You should have two containers, dukaconnect and database


__Run the following commands to set up your db__
```
docker exec -it database bash
psql

# then create a user and a database as usual with the credentials you entered in the env file earlier.

\q
exit
```

__Run the following commands to set up your app__
```
docker exec -it dukaconnect bash
# run the database migrations
./manage.py migrate
# load the soft drinks data
./manage.py loaddata drink.json
# create a super user
./manage.py createsuperuser

exit
```

In the nginx directory, there is an nginx configuration file.
Start an nginx container and pass that configuration file to it.
