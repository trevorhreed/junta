from libs.apps import BaseApp

class ReleasesApp(BaseApp):
	def get(self):
		self.render('/admin/releases')
