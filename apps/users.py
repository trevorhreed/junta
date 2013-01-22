from libs.cms import CmsApp
from libs.general import UserController
from google.appengine.api import users, memcache

class ProfileApp(CmsApp):
	def get(self):
		self.render('/users/profile')


class RegisterApp(CmsApp):
	def get(self):
		if UserController.user_is_registered():
			self.redirect('/')
		else:
			self.renderCmsApp('/users/register')


class SignInApp(CmsApp):
	def get(self):
		user = users.get_current_user()
		username = ""
		if user:
			username = user.email()
		self.context['username'] = username
		self.context['signout_uri'] = users.create_logout_url(dest_url='/signout')
		self.context['providers'] = UserController.get_signin_providers()
		self.renderCmsApp('/users/signin')

class SignOutApp(CmsApp):
	def get(self):
		user = users.get_current_user()
		if user:
			memcache.delete(user.email())
		self.redirect('/')
