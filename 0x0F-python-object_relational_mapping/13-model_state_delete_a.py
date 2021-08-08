#!/usr/bin/python3
'''delete states that contains letter a'''

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    eng = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(eng)

    ses = sessionmaker(bind=eng)()

    ses.query(State).filter(State.name.like('%a%')).\
        delete(synchronize_session=False)

    ses.commit()
    ses.close()
