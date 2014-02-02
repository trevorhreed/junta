from libs.cms import CmsApp

class LibraryApp(CmsApp):
	def get(self):
		self.renderCmsApp('/education/library_main')

	#def sort?

	def submit_entry(self):
		pass
