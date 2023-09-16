#!/usr/bin/python3
"""Contain a class definition of a State and an instance Base."""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Class representing a state in the database.

    Attributes:
        id (int): The unique identifier for the state.
        name (str): The name of the state.
    """

    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
