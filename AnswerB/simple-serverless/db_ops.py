from model import db


def dropdb():
    db.drop_all()


def createdb():
    db.create_all()


if __name__ == '__main__':
    db.create_all()
