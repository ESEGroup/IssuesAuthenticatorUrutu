import json

from datetime import datetime
from ..common.mail import send_email
from ..models import UsuarioSistema, UsuarioLab, AdministradorSistema, Delegate
from .. import app
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)


def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)

def generate_auth_token(user_id, expiration = 600000):
    s = Serializer(app.config['SECRET_KEY'], expires_in = expiration)
    return s.dumps({ 'id': user_id })

def verify_auth_token(token):
    s = Serializer(app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except SignatureExpired:
        return 'expired' # valid token, but expired
    except BadSignature:
        return 'invalid' # invalid token
    user = UsuarioSistema.obter(data['id'][0])
    return user

def is_authenticated(token):
    if (verify_auth_token(token) == ('expired' or 'invalid')):
        return False
    return True

def log_presence(ev):
    Delegate.log_presence(ev)

def presence_history(user):
    data = Delegate.presence_history(user)
    if(not data):
        return None
    print(data)
    return data

def check_presence(user):    
    data = Delegate.check_presence(user)
    if(data[0]==0):
        return None
    return data[1]

def check_preferences(user, lab_id):    
    preferences = Delegate.check_preferences(user, lab_id)
    if (not preferences):
        return None
    return preferences

def update_preferences(user, preferences):
    if(check_preferences(user, preferences['lab_id']) is None):    
        Delegate.add_preferences(user, preferences)
    else:
        Delegate.update_preferences(user, preferences)
