# CREATE DATABASE Film;
# CREATE USER 'student'@'%' IDENTIFIED WITH caching_sha2_password BY 'donotusethispassword';
# GRANT ALL PRIVILEGES ON *.* TO student@'%';
# GRANT ALL PRIVILEGES ON `Film`.* TO 'student'@'%' WITH GRANT OPTION;

# sudo apt install python3 python3-dev python3-pip
# sudo apt-get install python3-setuptools
# sudo apt-get install python3-pymysql
# pip3 install sqlalchemy
(Successfully installed sqlalchemy-1.3.15)
# pip3 install sqlalchemy-utils

from sqlalchemy import create_engine  
from sqlalchemy import Column, String  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

# url = "postgres://admin:donotusethispassword@aws-us-east-1-portal.19.dblayer.com:15813/compose"

# PyMySQL
# db = create_engine('mysql+pymysql://scott:tiger@localhost/foo')
# db = create_engine('mysql://{0}:{1}@{2}:{3}/{4}'.format(user, pass, host, port, db))

url = 'mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format('student', 'donotusethispassword', 'localhost', 3306, 'Film')

db = create_engine(url)
if not database_exists(db.url):
    create_database(db.url)
print('Conection to database Film:' + str(database_exists(db.url)))

base = declarative_base()

class Film(base):  
    __tablename__ = 'films'

    title = Column(String(30), primary_key=True)
    director = Column(String(20))
    year = Column(String(4))

Session = sessionmaker(db)  
session = Session()

base.metadata.create_all(db)

# Create 
doctor_strange = Film(title="Doctor Strange", director="Scott Derrickson", year="2016")
king_kong = Film(title="Kong: La Isla Calavera", director="Jordan Vogt-Roberts", year="2017") 
session.add(doctor_strange)
session.add(king_kong)
session.commit()

# Read
films = session.query(Film)  
for film in films:  
    print(film.title)

# Update
doctor_strange.title = "Some2016Film"  
session.commit()

# Delete
session.delete(doctor_strange)  
session.commit()  
