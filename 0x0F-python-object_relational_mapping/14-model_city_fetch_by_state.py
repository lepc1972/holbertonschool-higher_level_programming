#!/usr/bin/python3
"""list all cities of database"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2],
                                  argv[3]), pool_pre_ping=True)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    query = session.query(State, City).filter(State.id == City.state_id).order_by(City.id)
    for result in query:
        print("{}: ({}) {}".
              format(result.State.name, result.City.id, result.City.name))
    session.close()
