import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, nullable=False)
    favorites = relationship('Favorite', back_populates='user')

class Character(Base):
    __tablename__ = 'characters'
    character_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=False)
    image_url = Column(String(255))
    created_at = Column(DateTime, nullable=False)
    favorites = relationship('Favorite', back_populates='character')

class Planet(Base):
    __tablename__ = 'planets'
    planet_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=False)
    image_url = Column(String(255))
    created_at = Column(DateTime, nullable=False)
    favorites = relationship('Favorite', back_populates='planet')

class Favorite(Base):
    __tablename__ = 'favorites'
    favorite_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    character_id = Column(Integer, ForeignKey('characters.character_id'))
    planet_id = Column(Integer, ForeignKey('planets.planet_id'))
    created_at = Column(DateTime, nullable=False)
    user = relationship('User', back_populates='favorites')
    character = relationship('Character', back_populates='favorites')
    planet = relationship('Planet', back_populates='favorites')

if __name__ == '__main__':
    engine = create_engine('sqlite:///blog.db')
    Base.metadata.create_all(engine)
    render_er(Base, 'diagram.png')