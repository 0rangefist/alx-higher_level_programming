#!/usr/bin/python3
"""
This script prints a State object with the name
passed as an argument from the db, hbtn_0e_6_usa
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

    # name of state to query for
    state_name = sys.argv[4]

    # query to return list of states containing letter a
    state = (session
             .query(State)
             .filter_by(name=state_name)
             .first()
             )

    # print out the state if found
    if state is None:
        print("Not found")
    else:
        print(f"{state.id}")
