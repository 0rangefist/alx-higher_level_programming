#!/usr/bin/python3
"""
This script creates the state "California with the
city "San Francisco" to the db, hbtn_0e_100_usa
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # database connection details
    uname = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    port = 3306

    # create the database engine
    engine = create_engine(
        f'mysql+mysqldb://{uname}:{pwd}@localhost:{port}/{db}',
        pool_pre_ping=True)

    # create the tables according to schema using our models
    Base.metadata.create_all(engine)

    # create a session for changes to the db
    Session = sessionmaker(bind=engine)
    session = Session()

    # create new State "California"
    new_state = State(name="California")

    # create new City "San Francisco"
    new_city = City(name="San Francisco")

    # Associate city with the state
    new_state.cities.append(new_city)

    # Add the new State to the db
    session.add(new_state)
    session.commit()

    session.close()
