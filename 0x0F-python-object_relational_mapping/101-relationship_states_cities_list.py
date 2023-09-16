#!/usr/bin/python3
"""Lists all State objects, and corresponding City objects.

They are contained in the database hbtn_0e_101_usa.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, db_name),
        # echo=True, # uncomment to debug the queries
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = (
        session.query(State, City)
        .join(City)
        .order_by(State.id.asc())
        .order_by(City.id.asc())
        .all()
    )

    states = sorted(list(set([i[0] for i in results])),
                    key=lambda state: state.id)
    cities = [i[1] for i in results]

    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in cities:
            if city.state_id == state.id:
                print("    {}: {}".format(city.id, city.name))

    session.close()
