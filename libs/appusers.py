from google.appengine.ext import ndb
from libs import mdb
from google.appengine.api import users


def user_is_registered():
	user = users.get_current_user()
	if user:
		member = Member.query(Member.Handle == user.email()).get()
		if member:
			memcache.add(user.email(), member)
			return True
		else:
			return False
	else:
		print "we failed."
		return False

def register_user():
	pass

def get_signin_providers():
	return [
		('Google','/static/images/openid/google.png',users.create_login_url(dest_url='/register', federated_identity='https://www.google.com/accounts/o8/id')),
		('Yahoo','/static/images/openid/yahoo.png',users.create_login_url(dest_url='/register', federated_identity='yahoo.com')),
	]
