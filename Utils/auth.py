from werkzeug.security import safe_str_cmp
import hashlib


def authenticate(user, password):
    user_password = user.password.encode('utf-8')
    hashed_posted_password = hashlib.md5(password.encode('utf-8')).hexdigest()
    if user and safe_str_cmp(user_password, hashed_posted_password):
        return True