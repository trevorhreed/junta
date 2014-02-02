from libs.cms import CmsApp

class JuntaApp(CmsApp):
	def default(self, action):
		raise Exception("You cannot call this app directly.")
