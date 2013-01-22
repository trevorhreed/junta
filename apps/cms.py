from libs.apps import BaseApp
from libs.cms import CmsController

class CmsHandler(BaseApp):
	def get(self, path):
		CmsController.Route(path, self.response)
