from libs.apps import CmsApp
from libs.dal import Countries, Project, BudgetRange, DevelopmentSector, ProjectStates
from libs import projects

class VetApp(CmsApp):

	def get(self):
		phase_1_projects = Project.query(Project.Phase == ProjectPhases.Phase1)
		phase_2_projects = Project.query(Project.Phase == ProjectPhases.Phase2)
		phase_3_projects = Project.query(Project.Phase == ProjectPhases.Phase3)
		self.context = {
			'phase_1_projects':			phase_1_projects,
			'phase_1_project_count':	phase_1_projects.count(),
			'phase_2_projects':			phase_2_projects,
			'phase_2_project_count':	phase_2_projects.count(),
			'phase_3_projects':			phase_3_projects,
			'phase_3_project_count':	phase_3_projects.count(),
		}
		self.renderCmsApp('/projects/vetting_main')

	def get_project_profile(self):
		pass

	def upvote(self):
		pass

	def rate_initial(self):
		pass

	def rate_impact(self):
		pass

	def rate_innovation(self):
		pass

	def rate_sustainability(self):
		pass

	def post_comment(self):
		pass

	def mark_comment_as_helpful(self):
		pass


class SubmitApp(CmsApp):

	def get(self):
		var = 23
		self.context.update({
			'devsectors':		DevelopmentSector.query(),
			'budgetranges':		BudgetRange.query(),
			'countries':		Countries
		})
		self.renderCmsApp('/projects/submit_main')

	def submit(self):

		'''
		request.get('project[Title]')
		request.get('project[BriefAbstract]')
		request.get('project[LongAbstract]')
		request.get('project[HighImpactDescription]')
		request.get('project[SustainabilityDescription]')
		request.get('project[InnovationDescription]')
		request.get('project[BudgetDescription]')
		request.get('project[BudgetNotes]')
		mdb.Blob(request.POST['project[Image]'].value)
		request.POST['project[Image]'].type
		mdb.Blob(request.POST['project[BudgetWorksheet]'].value)
		request.POST['project[BudgetWorksheet]'].type
		request.get_all('project[CountryIds]')
		mdb.key(request.get('project[BudgetRange]'))
		mdb.key(request.get('project[DevelopmentSector]'))
		'''

		valid, msg = con.validate_project_submission(self.request)
		if valid:
			con.save_project_submission(self.request)
			self.renderCmsApp('/projects/submit_completed')
		else:
			self.context.update({
				'form_error':		msg,
				'devsectors':		DevelopmentSector.query(),
				'budgetranges':		BudgetRange.query(),
				'countries':		Countries
			})
			self.renderCmsApp('/projects/submit_main')


class PastApp(CmsApp):

	def get(self):
		self.renderCmsApp('index')
