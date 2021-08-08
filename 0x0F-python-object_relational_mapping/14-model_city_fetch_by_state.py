#!/usr/bin/python3
'''list all City objects from database hbtn_0e_14_usa'''

from sys import argv
from sqlalchemy import create_engine
from model_city import City
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    eng = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(eng)

    Session = sessionmaker(bind=eng)
    ses = Session()

    for c in ses.query(City).join(State).order_by(City.id).all():
        print("{}: ({}) {}".format(c.state.name, c.id, c.name))
    ses.close()
