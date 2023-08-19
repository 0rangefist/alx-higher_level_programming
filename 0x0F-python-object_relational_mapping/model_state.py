#!/usr/bin/python3
"""
This defines a State class that uses mysqlalchemy ORM to
work with a MySQL db in a pythonic (object oriented) way
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class that represents the
    states table with columns
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
