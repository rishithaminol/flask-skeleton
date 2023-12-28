import hashlib, json
from colored import fg, attr
from sqlalchemy.sql import text

from src.db import db_session, UserData

# Helper consonants
JSON_MIME_TYPE = 'application/json'

# Generate hash for the given string
def gen_user_pass_hash(password):
	return hashlib.sha512(password.encode()).hexdigest()

# Mostly needed by UserMixin in server.py
# this function is called on every request
def get_user_data(user_name, session_id):
	ds = db_session()

	if session_id:
		sql = text('''
			SELECT
				user_data.id_,
				user_data.name,
				user_data.password,
				user_data.access_level,
				session_data.session_id,
				session_data.expire,
				session_data.time
			FROM user_data
			LEFT JOIN session_data ON user_data.id_ = session_data.id_user
			WHERE session_id = :session_id AND session_data.expire > NOW()
		''')
	else:
		sql = text('''
			SELECT
				user_data.id_,
				user_data.name,
				user_data.password,
				user_data.access_level,
				null,
				null,
				null
			FROM user_data
			WHERE user_data.name = :name
		''')

	x = ds.execute(sql, {
		"session_id": session_id,
		"name": user_name
	}).first()

	return x

# Pay deep attention about this function in order to avoid
#	SQL Injection attacks.
#
# Do not let attacker to escape from this mechanism.
#	In other words do not let attacker to make this function return
#	True.
def check_user_credentials(user_name, pass_hash):
	x = db_session.query(UserData).\
				filter(UserData.name == user_name).\
				filter(UserData.password == pass_hash).first()

	# No user data
	if x is None:
		return False

	if x.name == user_name and x.password == pass_hash:
		return True

	return False

#
# Change administrative user password
# If the given user is not in the database return False
def change_password(user_name, new_password):
	___ = db_session
	dbses = ___()
	x = dbses.query(UserData). \
			filter_by(user_name=user_name).first()

	if x is None:
		return False

	x.password = gen_user_pass_hash(new_password)

	dbses.commit()

	return True

def green_output(str_):
	return "%s%s%s" %(fg(82), str_, attr(0))

# Return a dictionary which suitable for http json response
# The data returning from this function is suitable only for flask response
def common_response(data=None, status=200, message=None, err_msg=None):
    comm_respon = {}

    if data is not None and err_msg is None:
        comm_respon['data'] = data

    comm_respon['status'] = status

    if message is not None:
        comm_respon['message'] = message

    if err_msg is not None:
        comm_respon['err_msg'] = err_msg

    return json.dumps(comm_respon), comm_respon['status'], {'Content-Type': JSON_MIME_TYPE}

# Log out specific user from all of it's sessions
def logout_all_sessions(id_user):
	ds = db_session()

	sql = text('''
		UPDATE session_data
		SET expire = TIMESTAMP '2004-10-19 10:23:54'
		WHERE id_user = :id_user;
	''')
	ds.execute(sql, {
		"id_user": id_user
	})
	ds.commit()
	ds.close()

def logout_session(session_id):
	ds = db_session()

	sql = text('''
		UPDATE session_data
		SET expire = TIMESTAMP '2004-10-19 10:23:54'
		WHERE session_id = :session_id;
	''')
	ds.execute(sql, {
		"session_id": session_id
	})
	ds.commit()
	ds.close()

####
## ============================ [User Customizations] ============================
###
