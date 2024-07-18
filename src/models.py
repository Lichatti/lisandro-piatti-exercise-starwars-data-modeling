import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    firsname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250), unique = True)
    password = Column(String(250), unique = True)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    climate = Column(String(250))
    terrain = Column(String(250))
    population = Column(Integer)

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    hair_color = Column(String(250))
    eye_color = Column(String(250))
    skin_color = Column(String(250))


    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    people_id = Column(Integer, ForeignKey('people.id'))
    people = relationship(People)

    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
1