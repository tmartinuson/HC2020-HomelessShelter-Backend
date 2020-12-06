import sys

from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

from server.model.base import Base
from server.service.session import Session
from server.service.app import app

DATABASE = 'sqlite:///.\\database.db'

def main():
    engine = create_engine(DATABASE)
    Session.configure(bind=engine)

    try:
        Base.metadata.create_all(engine)
    except OperationalError:
        print('Could not connect to database')
        sys.exit(1)
    else:
        print('Connected to database')

    app.run()


if __name__ == '__main__':
    main()
