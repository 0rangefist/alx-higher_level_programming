#!/usr/bin/python3
"""
This defines a City class that uses mysqlalchemy ORM to
work with a MySQL db in a pythonic (object oriented) way
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """
    City class definition
    """
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
