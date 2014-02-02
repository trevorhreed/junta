from libs import mdb
from libs.apps import BaseApp
from libs.projects import Project, ProjectPhases, ProjectController


class ProjectsApp(BaseApp):

	def get(self):
		self.context['projects'] = Project.query()
		self.context['phases'] = ProjectPhases.TypesByKey
		self.render('/admin/projects/projects_main')

	def update_phase(self):
		project_id = self.request.get('project_id', None)
		phase_id = self.request.get_range('phase_id', ProjectPhases.Phase1, ProjectPhases.Phase3, ProjectPhases.Phase1)
		ProjectController.update_project_phase(project_id, phase_id)
		self.write("Updated project '"+str(project_id)+"' to phase '"+str(phase_id)+"'.")
