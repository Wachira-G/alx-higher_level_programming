#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter a.

Deletes from the database hbtn_0e_6_usa.
"""


if __name__ == "__main__":

    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    args = sys.argv
    mysql_username = args[1]
    mysql_password = args[2]
    database_name = args[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            mysql_username, mysql_password, database_name
        ),
        pool_pre_ping=True,
    )

    Session = sessionmaker(bind=engine)
    session = Session()
    records = session.query(State).filter(State.name.ilike("%a%")).all()

    for record in records:
        session.delete(record)

    session.commit()
