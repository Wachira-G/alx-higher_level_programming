#!/usr/bin/python3
"""Contain a class definition of a State and an instance Base."""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base  # City

# Base = declarative_base()


class State(Base):
    """Class representing a state in the database.

    Attributes:
        id (int): The unique identifier for the state.
        name (str): The name of the state.
        cities(relationship): links the states table with the cities tables
    """

    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete",
                          back_populates="state")
