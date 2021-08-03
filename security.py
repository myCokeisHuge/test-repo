from werkzeug.security import safe_str_cmp
from app_code.models.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username)  # get username if not present return None
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):  # 'payload = JWT token
    user_id = payload['identity']  # extract userid from payload
    return UserModel.find_by_id(user_id)
