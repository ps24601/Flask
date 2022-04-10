from models.user import UserModel
import hmac

def authenticate(username,password):
    user = UserModel.findByUsername(username)
    if user and hmac.compare_digest(user.password,password):
        return user

# payload will be JWT
def identity(payload):
    userid = payload['identity']
    return UserModel.findById(userid)