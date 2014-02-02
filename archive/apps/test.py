from libs.cms import CmsApp

from doms import sysprops
from google.appengine.ext import ndb

class TestApp(CmsApp):

	def get(self):
		self.renderCmsApp('/test/page')

	def show_property(self):
		sp = sysprops.get(sysprops.Phase1_MaximumProjects)
		self.write(sp.key.id() + ": " + sp.Value)

	def create_property(self):
		sp = sysprops.set(sysprops.Phase1_MaximumProjects, 7)
		self.write(sp.Value)
