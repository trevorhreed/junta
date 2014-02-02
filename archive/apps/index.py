from apps import JuntaApp


class IndexApp(JuntaApp):
	def start(self):
		pass
		#self.view_prefix = ''

	def default(self, action):
		self.redirect('/projects/vetting')



__doc__ = IndexApp
