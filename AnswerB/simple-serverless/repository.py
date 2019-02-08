from typing import Union, List, Dict, Optional

from model import User, db


class Error:
    msg: str
    status_code: int

    def __init__(self, msg, code):
        self.msg = msg
        self.status_code = code


def get_all_users() -> List[Dict[str, Union[int, str]]]:
    users = User.query.all()
    users = list(map(lambda u: u.to_json(), users))
    return users


def search_user_with_id(id: int) -> User:
    return User.query.get(id)


def search_user_with_email(email: str) -> User:
    return User.query.filter(
        User.email == email
    ).first()


def check_credentials(email: str, password: str) -> Optional[User]:
    user = search_user_with_email(email)
    if not user:
        return None
    return user if user.verify_password(password) else None


def add_new_user(name: str, email: str, password: str) -> Union[User, Error]:
    user = search_user_with_email(email)
    if user:
        return Error(msg="user with this email already exists", code=400)

    try:
        new_user = User(name, email, password)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    except Exception as ex:
        return Error(msg=str(ex), code=500)
