#!/usr/bin/python3
"""
This script deletes all State objects with a name
containing the letter a from the db, hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
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

    # create a session for querying
    Session = sessionmaker(bind=engine)
    session = Session()

    # query to return states with name containing letter 'a'
    states = (session
              .query(State)
              .filter(State.name.contains("a"))
              .all()
              )

    # delete all found states matching the query criteria
    for state in states:
        session.delete(state)
    session.commit()
    session.close()
