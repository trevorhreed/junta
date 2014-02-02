import core, webapp2

app = webapp2.WSGIApplication([

		('/admin/',								'apps.admin.trustees.TrusteeVettingApp'),

		('/admin/cms/',							'apps.admin.cms.PagesApp'),
		('/admin/cms/layouts',					'apps.admin.cms.LayoutsApp'),

		('/admin/projects/',					'apps.admin.projects.ProjectsApp'),

		('/admin/utils/docs',					'apps.admin.utils.DocumentApp'),
		('/admin/utils/devsectors',				'apps.admin.utils.DevSectorApp'),
		('/admin/utils/budgetranges',			'apps.admin.utils.BudgetRangeApp'),
		('/admin/utils/setup',					'apps.admin.utils.SetupApp'),

		('/admin/releases',						'apps.admin.misc.ReleasesApp')

	], debug=core.APP_DEBUG)
