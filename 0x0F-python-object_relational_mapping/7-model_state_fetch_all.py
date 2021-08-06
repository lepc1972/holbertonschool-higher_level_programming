#!/usr/bin/python3
"""list the states of database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    connection = 'mysql+mysqldb://{}:{}@localhost:3306/{}'

    engine = create_engine(connection.format(user_name, password, db_name),
                           pool_pre_ping=True)
    Ses = sessionmaker(bind=engine)
    session = Ses()
    search = session.query(State).order_by(State.id).all()
    for some in search:
        print("{}: {}".format(some.id, some.name))
