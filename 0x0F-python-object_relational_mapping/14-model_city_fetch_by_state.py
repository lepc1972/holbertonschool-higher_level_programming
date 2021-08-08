#!/usr/bin/python3
"""
script that prints all City objects from the database
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2],
                                  argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    query = session.query(State, City).filter(State.id == City.state_id).all()
    for result in query:
        print("{}: ({}) {}".
              format(result.State.name, result.City.id, result.City.name))
    session.close()
