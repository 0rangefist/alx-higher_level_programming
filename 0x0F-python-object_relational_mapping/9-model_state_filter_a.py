#!/usr/bin/python3
"""
This script prints all State objects that
contain the letter a from db, hbtn_0e_6_usa
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

    # query to return list of states containing letter a
    states = (session
              .query(State)
              .filter(State.name.like('%a%'))
              .order_by(State.id)
              .all()
              )

    # print out the states
    for state in states:
        print(f"{state.id}: {state.name}")
