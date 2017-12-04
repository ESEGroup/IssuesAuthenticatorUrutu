import json

from flask import request, jsonify
from .. import app, controllers
from datetime import datetime
from collections import namedtuple

def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)


@app.route('/delegate/token')
def get_auth_token():
	r = request.get_json()
	login = r['login']
	pwd = r['senha']
	user = controllers.autenticar(login, pwd) 
	if(user is not None):
		token = controllers.generate_auth_token(user)
		return jsonify({'token': token.decode('ascii')})
	return jsonify({'e': 'Error generating token.'})


@app.route('/delegate/verify_token')
def get_verify_token():
	r = request.get_json()
	token = r['token']
	user = controllers.verify_auth_token(token)
	if(user is 'invalid'):
		return jsonify({'e': "Token does not match any user."})
	elif(user is 'expired'):
		return jsonify({'e': "Token expired."})	
	return jsonify({'user_id': user.id, 'username': user.login})


@app.route('/delegate/check_presence', methods=['POST'])
def check_presence():
	r = request.get_json()
	token = r['token']
	if(controllers.is_authenticated(token)):
		user = controllers.verify_auth_token(token)
		lab_id = controllers.check_presence(user)
		if(lab_id is not None):	
			return jsonify({'e': 'User is currently at lab '+ str(lab_id) +'.'})
		return jsonify({'e': 'User is absent.'})
	return jsonify({'e':'Error logging presence.'})


@app.route('/delegate/log_presence', methods=['POST'])
def log_presence():
	r = request.get_json()
	ev = namedtuple('ev','user_id lab_id data chegada')
	token = r['token']
	ev.lab_id = r['lab_id']
	ev.chegada = r['chegada']
	ev.data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	if(controllers.is_authenticated(token)):
		ev.user_id = controllers.verify_auth_token(token).id
		controllers.log_presence(ev)	
		return jsonify({'e': 'Presence logged successfully.'})
	return jsonify({'e':'Error logging presence.'})


@app.route('/delegate/presence_history', methods=['POST'])
def presence_history():
	r = request.get_json()
	token = r['token']

	if(controllers.is_authenticated(token)):
		user = controllers.verify_auth_token(token)
		history = controllers.presence_history(user)
		if(history is not None):
			return jsonify({'history':history})	
		return jsonify({'e': 'No history found for given user.'})
	return jsonify({'e':'You need authentication.'})


@app.route('/delegate/check_preferences')
def check_preferences():
	r = request.get_json()
	token = r['token']
	lab_id = r['lab_id']
	if(controllers.is_authenticated(token)):
		user = controllers.verify_auth_token(token)
		preferences = controllers.check_preferences(user, lab_id)	
		return jsonify({'preferences':preferences})
	return jsonify({'e':'Error checking preferences.'})


@app.route('/delegate/update_preferences', methods=['POST'])
def update_preferences():
	r = request.get_json()
	token = r['token']
	preferences = r['preferences']
	if(controllers.is_authenticated(token)):
		user = controllers.verify_auth_token(token)
		controllers.update_preferences(user, preferences)
		return jsonify({'e': 'Preferences updated successfully.'})
	return jsonify({'e':'Error updating preferences.'})
