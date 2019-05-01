from . import login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    id = user.get("user_id")
    return int(id)

class User(UserMixin):
    user = {
        "user_id": 1,
        "username": "SPG",
        "password": "w3w3"
    }
    user_id = user.get('user_id')
    username = user.get('username')
    password = user.get('password')