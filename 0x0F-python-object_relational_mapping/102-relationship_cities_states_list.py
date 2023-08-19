#!/usr/bin/python3
"""
This script lists all City objects
contained in the db, hbtn_0e_100_usa
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
        f'mysql://{uname}:{pwd}@localhost:{port}/{db}',
        pool_pre_ping=True)

    # create the tables according to schema using our models
    Base.metadata.create_all(engine)

    # create a session for changes to the db
    Session = sessionmaker(bind=engine)
    session = Session()

    # query to grab all state objects
    cities = session.query(City).order_by(City.id).all()

    # print the cities, and associated state
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    session.close()
