
SOURCES:

--FLASK--
https://oregonstate.instructure.com/courses/1821208/pages/learn-using-python-and-flask-framework

https://flask.palletsprojects.com/en/1.1.x/

https://github.com/osu-cs340-ecampus/flask-starter-app

start the virtual env:
source venv/bin/activate

start the website:
python -m flask run -h 0.0.0.0 -p 5000

--MYSQL--

How to add a new user and add privliges:
(this is what I used)

https://howchoo.com/webdev/how-to-add-a-mysql-user-and-grant-privileges

Load in sql data:

mysql -u newuser -p  stonks < /Users/orelyehuda/stonksweb/database/stonks_db.sql
