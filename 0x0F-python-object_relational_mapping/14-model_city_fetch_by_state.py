#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa."""

if __name__ == "__main__":

    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City

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

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities_states_query = (
        session.query(State.name, City.id, City.name)
        .filter(State.id == City.state_id)
        .order_by(City.id.asc())
        .all()
    )

    for result in cities_states_query:
        state_name = result[0]
        city_id = result[1]
        city_name = result[2]
        print("{}: ({}) {}".format(state_name, city_id, city_name))

    session.close()
