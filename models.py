# imports
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, relationship
from sqlalchemy.sql.expression import text
from typing import List, Optional
from sqlalchemy.sql.sqltypes import TIMESTAMP, DateTime

# do i need to import Base here? or does this clash with the base model below it?
from database import Base

# define the Base model
class Base(DeclarativeBase):
    pass

#! PARENT MODELS ----------------------------------------------------------------

# USER MODEL - PARENT
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    created_timestamp = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

# SONG MODEL - PARENT
class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    name = Column(String, nullable=False)
    #could add duration here? - can use this to test "updating" crud

# ARTIST MODEL - PARENT
class Artist(Base):
    __tablename__ = "artists"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    name = Column(String, nullable=False)
    #could add image here? - can use this to test "updating" crud

# ALBUM MODEL - PARENT
class Album(Base):
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    name = Column(String, nullable=False)
    release_date = Column(DateTime, nullable=True)
    #could add image here? - can use this to test "updating" crud

# PLAYLSIT MODEL - PARENT
class Playlist(Base):
    __tablename__ = "playlists"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    name = Column(String, nullable=False)
    date_created_timestamp = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    created_by_user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    #parent to parent - one user to many playlists

    #place relationship here

#! CHILD/BRIDGE MODELS -----------------------------------------------------------------------
