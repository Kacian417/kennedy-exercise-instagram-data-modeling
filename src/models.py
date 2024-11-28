import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, unique=False, nullable=False)
    first_name = Column(String, unique=False, nullable=False)
    last_name = Column(String, unique=False, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String, unique=False, nullable=True)
    gender = Column(String, unique=False, nullable=False)

class Post(Base):
    __tablename__ = 'posts'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=False, nullable=False)
    body = Column(String, unique=False, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)

    def to_dict(self):
        return {}
    
class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    body = Column(String, unique=False, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship(Post)

class Follow(Base):
    __tablename__ = "follows"
    
    id = Column(Integer, primary_key=True)
    following_user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)
    followed_user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)




## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
