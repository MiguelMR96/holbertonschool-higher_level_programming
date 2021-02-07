#!/usr/bin/python3
"""[summary]
"""
if __name__ == "__main__":
    import sys
    import sqlalchemy
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for i in session.query(State).filter(State.name.like(sys.argv[4])).all():
        try:
            print("{}".format(state.id))
        except:
            print("Not found")
    session.close()
