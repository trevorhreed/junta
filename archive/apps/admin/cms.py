import core
import os
import webapp2
from Application_Junta import app as JuntaApp
from google.appengine.ext import ndb
from google.appengine.api import memcache
from libs import mdb
from libs.apps import BaseApp
from libs.cms import CmsPage, CmsLayout, CmsPageTypes, CmsController

class PagesApp(BaseApp):

	def get(self):
		self.context['parents'] = self.context['sitemap'] = CmsController.GetSitemapList()
		self.context['layouts'] = CmsController.GetLayoutList()
		self.context['page_types'] = CmsPageTypes.TypesByKey
		self.context['modules'] = self._get_site_modules()

		page = CmsPage.query().get()
		is_saved = True
		if page is None:
			page = CmsPage()
			is_saved = False

		self.context['page'] = page
		self.context['is_saved'] = is_saved
		self.render('/admin/cms/pages_main')

	def new(self):
		parentpage_id = self.request.get('parentpage_id', None)
		page = CmsPage()
		page.Name = "New Name"
		page.Path = "/newpage"
		page.Link = "New Page"
		page.Sort = "New Page"
		page.Content = "New Page Content"
		page.Enabled = True
		page.SiteMenu = True
		self.context['page'] = page
		self.context['is_saved'] = False
		self.context['parent_page_key'] = parentpage_id
		self.context['parents'] = CmsController.GetSitemapList()
		self.context['layouts'] = CmsController.GetLayoutList()
		self.context['page_types'] = CmsPageTypes.TypesByKey
		self.context['modules'] = self._get_site_modules()
		self.render('/admin/cms/pages_edit')

	def edit(self):
		page_id = self.request.get('page_id', None)
		page = CmsPage.get(page_id)
		self.context['page'] = page
		self.context['is_saved'] = True
		if page.ParentPage:
			parent_page_key = page.ParentPage.urlsafe()
		else:
			parent_page_key = None
		self.context['parent_page_key'] = parent_page_key
		self.context['parents'] = CmsController.GetSitemapList()
		self.context['layouts'] = CmsController.GetLayoutList()
		self.context['page_types'] = CmsPageTypes.TypesByKey
		self.context['modules'] = self._get_site_modules()
		self.render('/admin/cms/pages_edit')

	def save(self):
		page_id = self.request.get('page[id]', None)
		if page_id == 'new':	page = CmsPage()
		else:					page = CmsPage.get(page_id)
		page.stuff(self.request)
		page.put()
		self.context['page'] = page
		self.context['is_saved'] = True
		if page.ParentPage:
			parent_page_key = page.ParentPage
		else:
			parent_page_key = None
		self.context['parent_page_key'] = parent_page_key
		self.context['parents'] = CmsController.GetSitemapList()
		self.context['layouts'] = CmsController.GetLayoutList()
		self.context['page_types'] = CmsPageTypes.TypesByKey
		self.context['modules'] = self._get_site_modules()
		self.context['sitemap'] = CmsController.GetSitemapList()
		self.render([
			'/admin/cms/pages_list',
			'/admin/cms/pages_edit',
		])

	def delete(self):
		page_id = self.request.get('page_id', None)
		mdb.delete(page_id)
		self.context['sitemap'] = CmsController.GetSitemapList()
		self.render([
			'/admin/cms/pages_list',
			'/admin/cms/pages_edit',
		])

	def _get_site_modules(self):
		return [
			'/vetting',
			'/submit',
			'/past',
			'/library',
			'/register',
			'/profile',
			'/signin',
			'/signout',
			'/test',
		]


class LayoutsApp(BaseApp):

	def get(self):
		self.context['layouts'] = CmsController.GetLayoutList()

		layout = CmsLayout.query().get()
		is_saved = True
		if layout is None:
			layout = CmsLayout()
			is_saved = False

		self.context['layout'] = layout
		self.context['is_saved'] = is_saved
		self.render('/admin/cms/layouts_main')

	def new(self):
		layout = CmsLayout()
		layout.Name = "New Layout"
		layout.Content = ""
		self.context['layout'] = layout
		self.context['is_saved'] = False
		self.render('/admin/cms/layouts_edit')

	def edit(self):
		layout_id = self.request.get('layout_id', None)
		layout = CmsLayout.get(layout_id)
		self.context['layout'] = layout
		self.context['is_saved'] = True
		self.render('/admin/cms/layouts_edit')

	def save(self):
		layout_id = self.request.get('layout[id]', None)
		if layout_id == 'new':
			layout = CmsLayout()
		else:
			layout = CmsLayout.get(layout_id)
		layout.stuff(self.request)
		layout.put()
		self.context['layouts'] = CmsController.GetLayoutList()
		self.context['is_saved'] = True
		self.render('/admin/cms/layouts_list')

	def delete(self):
		layout_id = self.request.get('layout_id', None)
		mdb.delete(layout_id)
		self.context['layouts'] = CmsController.GetLayoutList()
		self.render(['/admin/cms/layouts_list', '/admin/cms/layouts_edit'])
