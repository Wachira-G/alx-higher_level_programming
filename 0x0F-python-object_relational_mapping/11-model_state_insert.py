#!/usr/bin/python3
"""Add the State object “Louisiana” to the database hbtn_0e_6_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


args = sys.argv
mysql_username = args[1]
mysql_password = args[2]
database_name = args[3]

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
    new_state = State()
    new_state.name = "Louisiana"
    session.add(new_state)
    session.commit()
    state = session.query(State).filter(State.name == "Louisiana").first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
