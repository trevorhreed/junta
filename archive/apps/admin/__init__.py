from libs.apps import BaseApp

class AdminApp(BaseApp):
	def default(self, action):
		raise Exception("You cannot call this app directly.")
