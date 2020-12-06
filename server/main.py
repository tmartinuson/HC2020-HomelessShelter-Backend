import sys


def main():
    engine = create_engine(db)
    Session.configure(bind=engine)

    try:
        Base.metadata.create_all(engine)
    except OperationalError:
        print('Could not connect to database')
        sys.exit(1)
    else:
        print('Connected to database')


if __name__ == '__main__':
    main()
