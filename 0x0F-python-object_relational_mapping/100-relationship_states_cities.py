#!/usr/bin/python3
"""Creates the State “California” with the City “San Francisco”.

this is from the database hbtn_0e_100_usa.
"""

if __name__ == "__main__":

    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import State, Base
    from relationship_city import City

    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, db_name),
        # pool_pre_ping=True,
        # echo=True, # used to observe the queries to db
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)

    session.add(san_francisco)
    session.commit()
    session.close()
