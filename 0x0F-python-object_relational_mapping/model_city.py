#!/usr/bin/python3
"""Contain the class definition of a city."""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

Base = declarative_base()


class City(Base):
    """Class representing a city in the database.

    Attributes:
        id (int): The unique identifier for the city.
        name (str): The name of the city.
        state_id (int): The foreign key referencing the state's id.

        state (relationship): The relationship btwn the City and State models.
    """

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    # define the relationship with state:
    # state = relationship("State", back_populates="cities")
