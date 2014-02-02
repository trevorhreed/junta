from libs.apps import BaseApp
from libs.general import Document
from libs.projects import DevelopmentSector, Project

class DocumentFetcher(BaseApp):
	def get(self, doc_id):
		doc = Document.get(doc_id)
		if doc:
			self.response.headers['Content-Type'] = str(doc.Mime)
			self.response.out.write(doc.Contents)
			return
		else:
			print "failed."


class ProjectImageFetcher(BaseApp):
	def get(self, project_id):
		project = Project.get(project_id)
		if project:
			self.response.headers['Content-Type'] = str(project.ImageMime)
			self.response.out.write(project.Image)
			return
		else:
			print "failed."


class DevSectorImageFetcher(BaseApp):
	def get(self, ds_id):
		devsector = DevelopmentSector.get(ds_id)
		if devsector:
			self.response.headers['Content-Type'] = str(devsector.ImageMime)
			self.response.out.write(devsector.Image)
			return
		else:
			print "failed."
