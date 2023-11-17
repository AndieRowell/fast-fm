# imports
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, relationship
from sqlalchemy.sql.expression import text
from typing import List, Optional
from sqlalchemy.sql.sqltypes import TIMESTAMP

# do i need to import Base here? or does this clash with the base model below it?
from database import Base

# define the Base model
class Base(DeclarativeBase):
    pass

# User model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    created_timestamp = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

# Song model
class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    name = Column(String, nullable=False)
    #could add duration here?
