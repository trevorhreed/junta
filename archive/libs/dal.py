from google.appengine.ext import db, ndb

################################################################################
# Utility Functions

def to_blob(file):
	return db.Blob(file)

def to_key(id):
	return ndb.Key(urlsafe=id)


################################################################################
# Enumerations

Countries = [
	'United States of America',
	'United Kingdom',
	'Sweden'
]

################################################################################
# Models

class BaseModel(ndb.Model):
	def id(self):
		return self.key.urlsafe()

	@staticmethod
	def delete_by_id(id):
		ndb.Key(urlsafe=id).delete()

class DevelopmentSector(BaseModel):
	Name			= ndb.StringProperty()
	Image			= ndb.BlobProperty()
	ImageMime		= ndb.StringProperty()

	def stuff(self, request):
		self.Name		= request.get('devsector[Name]',	default_value=self.Name)
		self.Image		= to_blob(request.POST['devsector[Image]'].value)
		self.ImageMime	= request.POST['devsector[Image]'].type

class ProjectStates(object):
	Pending			= 1
	Phase1Queue		= 2
	Phase1			= 3
	Phase2Queue		= 4
	Phase2			= 5
	Phase3Queue		= 6
	Phase3			= 7
	Phase4Queue		= 8
	Phase4			= 9
	Funded			= 10
	Retired			= 11

class BudgetRange(BaseModel):
	Name						= ndb.StringProperty()
	Min							= ndb.StringProperty()
	Max							= ndb.StringProperty(default=None)

	def stuff(self, request):
		self.Name		= request.get('budgetrange[Name]',		default_value=self.Name)
		self.Min		= request.get('budgetrange[Min]',		default_value=self.Min)
		self.Max		= None if request.get('budgetrange[Max]', default_value='None') == '' else request.get('budgetrange[Max]', default_value=self.Max)

	def get_label(self):
		label = self.Name
		if not self.Max:
			label += " (" + self.Min + "+)"
		else:
			label += " (" + self.Min + " - " + self.Max + ")"
		return label

class Project(BaseModel):
	Title						= ndb.StringProperty()
	DevelopmentSector			= ndb.KeyProperty(DevelopmentSector)
	Phase						= ndb.IntegerProperty(default=ProjectPhases.Phase1)
	Countries					= ndb.StringProperty(repeated=True)
	Image						= ndb.BlobProperty()
	ImageMime					= ndb.StringProperty()
	BriefAbstract				= ndb.TextProperty()
	LongAbstract				= ndb.TextProperty()
	HighImpactDescription		= ndb.TextProperty()
	SustainabilityDescription	= ndb.TextProperty()
	InnovationDescription		= ndb.TextProperty()
	BudgetDescription			= ndb.TextProperty()
	BudgetWorksheet				= ndb.BlobProperty()
	BudgetWorksheetMime			= ndb.StringProperty()
	BudgetNotes					= ndb.StringProperty()
	BudgetRange					= ndb.KeyProperty(BudgetRange)
	When						= ndb.DateTimeProperty(auto_now=True)

	def stuff(self, request):
		self.Title						= request.get('project[Title]',						default_value=self.Title)
		self.Phase						= int(request.get('project[Phase]',					default_value=self.Phase))
		self.BriefAbstract				= request.get('project[BriefAbstract]',				default_value=self.BriefAbstract)
		self.LongAbstract				= request.get('project[LongAbstract]',				default_value=self.LongAbstract)
		self.HighImpactDescription		= request.get('project[HighImpactDescription]',		default_value=self.HighImpactDescription)
		self.SustainabilityDescription	= request.get('project[SustainabilityDescription]',	default_value=self.SustainabilityDescription)
		self.InnovationDescription		= request.get('project[InnovationDescription]',		default_value=self.InnovationDescription)
		self.BudgetDescription			= request.get('project[BudgetDescription]',			default_value=self.BudgetDescription)
		self.BudgetNotes				= request.get('project[BudgetNotes]',				default_value=self.BudgetNotes)
		self.Image						= mdb.Blob(request.POST['project[Image]'].value)
		self.ImageMime					= request.POST['project[Image]'].type
		self.BudgetWorksheet			= mdb.Blob(request.POST['project[BudgetWorksheet]'].value)
		self.BudgetWorksheetMime		= request.POST['project[BudgetWorksheet]'].type
		self.Countries					= request.get_all('project[CountryIds]')
		self.BudgetRange				= ndb.Key(urlsafe=request.get('project[BudgetRange]'))
		self.DevelopmentSector			= ndb.Key(urlsafe=request.get('project[DevelopmentSector]'))

class Comment(BaseModel):
	Project						= ndb.KeyProperty(Project)
	Member						= ndb.KeyProperty(Member)
	Comment						= ndb.TextProperty()
	When						= ndb.DateTimeProperty(auto_now=True)
	Helpful						= ndb.BooleanProperty(default=False)

class UserRatings(BaseModel):
	Project						= ndb.KeyProperty(Project)
	Member						= ndb.KeyProperty(Member)

	Vote						= ndb.IntegerProperty()
	InitialRating				= ndb.IntegerProperty()
	ImpactRating				= ndb.IntegerProperty()
	InnovationRating			= ndb.IntegerProperty()
	SustainabilityRating		= ndb.IntegerProperty()

class Member(BaseModel):
	Handle					= ndb.StringProperty()
	Email					= ndb.StringProperty()
	VoteCount				= ndb.IntegerProperty()
	ReferredBy				= ndb.KeyProperty('Member')
	HelpfulCommentCount		= ndb.IntegerProperty()
	When					= ndb.DateTimeProperty(auto_now=True)

class SystemProperty(BaseModel):
	Value		= ndb.StringProperty()

class Document(BaseModel):
	Name			= ndb.StringProperty()
	Description		= ndb.StringProperty()
	Scheme			= ndb.StringProperty()
	Identifier		= ndb.StringProperty()
	Mime			= ndb.StringProperty()
	Contents		= ndb.BlobProperty()

	def stuff(self, request):
		self.Name			= request.get('doc[Name]',				default_value=self.Name)
		self.Description	= request.get('doc[Description]',		default_value=self.Description)
		self.Scheme			= request.get('doc[Scheme]',			default_value=self.Scheme)
		self.Identifier		= request.get('doc[Identifier]',		default_value=self.Identifier)
		self.Contents		= mdb.Blob(request.POST['doc[File]'].value)
		self.Mime			= request.POST['doc[File]'].type

	def get_base64(self):
		return base64.b64encode(self.Contents)

class CmsPageTypes(object):
	Content		= 1
	Module		= 2
	Link		= 3

	TypesByName = {
		'Content':		1,
		'Module':		2,
		'Link':			3,
	}

	TypesByKey = {
		1:	'Content',
		2:	'Module',
		3:	'Link',
	}

class CmsLayout(BaseModel):
	Name				= ndb.StringProperty()
	Content				= ndb.TextProperty()
	UsedPlaceholders	= ndb.StringProperty(repeated=True)

	def stuff(self, request):
		self.Name		= request.get('layout[Name]',		default_value=self.Name)
		self.Content	= request.get('layout[Content]',	default_value=self.Content)

	def put(self, **kwargs):
		self.preput()
		super(CmsLayout, self).put(**kwargs)

	def preput(self):
		self.UsedPlaceholders = []
		regex = "({{[^}]*}})"
		for result in re.finditer(regex, self.Content):
			self.UsedPlaceholders.append(result.groups()[0])

class CmsPage(BaseModel):
	Name			= ndb.StringProperty()
	Path			= ndb.StringProperty()
	Content			= ndb.TextProperty()
	Link			= ndb.StringProperty()
	Sort			= ndb.StringProperty()
	ParentPage		= ndb.KeyProperty(kind='CmsPage')
	Layout			= ndb.KeyProperty(kind=CmsLayout)
	Enabled			= ndb.BooleanProperty(default=True)
	SiblingMenu		= ndb.BooleanProperty(default=True)
	SiteMenu		= ndb.BooleanProperty(default=True)
	Type			= ndb.IntegerProperty()

	def children(self):
		return CmsPage.query(CmsPage.ParentPage == self.key).order(CmsPage.Sort)

	def stuff(self, request):
		self.Name			= request.get('page[Name]',				default_value=self.Name)
		self.Path			= request.get('page[Path]',				default_value=self.Path)
		self.Content		= request.get('page[Content]',			default_value=self.Content)
		self.Link			= request.get('page[Link]',				default_value=self.Link)
		self.Sort			= request.get('page[Sort]',				default_value=self.Sort)
		self.Enabled		= bool(request.get('page[Enabled]',		default_value=self.Enabled))
		self.SiblingMenu	= bool(request.get('page[SiblingMenu]',	default_value=self.SiblingMenu))
		self.SiteMenu		= bool(request.get('page[SiteMenu]',	default_value=self.SiteMenu))
		self.Type			= int(request.get('page[Type]',			default_value=self.Type))
		self.Layout			= None if request.get('page[Layout]', 'None') == 'None' else mdb.key_from_id(request.get('page[Layout]'))
		self.ParentPage		= None if request.get('page[ParentPage]', 'None') == 'None' else mdb.key_from_id(request.get('page[ParentPage]'))
