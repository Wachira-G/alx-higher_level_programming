#!/usr/bin/python3
"""Prints the State object with the name passed as argument.

Prints from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


args = sys.argv
mysql_username = args[1]
mysql_password = args[2]
database_name = args[3]
state_name_to_search = args[4]

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            mysql_username, mysql_password, database_name
        ),
        pool_pre_ping=True,
    )
    # create session
    Session = sessionmaker(bind=engine)
    session = Session()
    state = (
        session.query(State)
        .filter(State.name == state_name_to_search)
        .order_by(State.id.asc())
        .first()
    )
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
