import core, webapp2
from webapp2_extras import routes

app = webapp2.WSGIApplication([

		('/vetting',										'apps.projects.VetApp'),
		('/submit',											'apps.projects.SubmitApp'),
		('/past',											'apps.projects.PastApp'),

		('/library',										'apps.education.LibraryApp'),

		('/register',										'apps.users.RegisterApp'),
		('/profile',										'apps.users.ProfileApp'),
		('/signin',											'apps.users.SignInApp'),
		('/signout',										'apps.users.SignOutApp'),

		('/test',											'apps.test.TestApp'),

		webapp2.Route('/utils/docs/<doc_id>',				'apps.utils.DocumentFetcher'),
		webapp2.Route('/utils/projectimage/<project_id>',	'apps.utils.ProjectImageFetcher'),
		webapp2.Route('/utils/dsimages/<ds_id>',			'apps.utils.DevSectorImageFetcher'),

		webapp2.Route('<path:.*>',							'apps.cms.CmsHandler')


	], debug=core.APP_DEBUG)
