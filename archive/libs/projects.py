from libs.dal import Member, Project, ProjectPhases, to_blob, to_key

def submit_project(
		title,
		image,
		image_mime,
		budget_worksheet,
		budget_worksheet_mime,
		budget_range,
		development_sector,
		country_ids=[],
		brief_abstract='',
		long_abstract='',
		high_impact_description='',
		sustainability_description='',
		innovation_description='',
		budget_description='',
		budget_notes='',
	):

	project = Project()

	project.State						= ProjectStates.Pending
	project.Title						= title
	project.BriefAbstract				= brief_abstract
	project.LongAbstract				= long_abstract
	project.HighImpactDescription		= high_impact_description
	project.SustainabilityDescription	= sustainability_description
	project.InnovationDescription		= innovation_description
	project.BudgetDescription			= budget_description
	project.BudgetNotes					= budget_notes
	project.Image						= to_blob(image)
	project.ImageMime					= image_mime
	project.BudgetWorksheet				= to_blob(budget_worksheet)
	project.BudgetWorksheetMime			= budget_worksheet_mime
	project.Countries					= country_ids
	project.BudgetRange					= to_key(budget_range)
	project.DevelopmentSector			= to_key(development_sector)

	project.put()

def upvote(project_id, member, vote):
	pass

def rate_project_generally(project_id, member, rating):
	pass

def rate_project_on_impact(project_id, member, rating):
	pass

def rate_project_on_innovation(project_id, member, rating):
	pass

def rate_project_on_sustainability(project_id, member, rating):
	pass

def post_comment(project_id, member, comment):
	pass

def mark_comment_as_helpful(comment_id):
	pass

def update_project_phase_if_qualifies(project_id):
	pass

def update_project_phase(project_id, user, phase_id):
	project = Project.get_by_id(project_id)
	project.Phase = phase_id
	project.put()
