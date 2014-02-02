import os
import re
import jinja2
import core

from google.appengine.api import users
from google.appengine.ext import db
from libs.apps import BaseApp
from libs import appusers
from libs.views import JuntaTemplateLoader


def Route(path, response):
	page = CmsPage.query(CmsPage.Path == path).get()
	if page:
		layout = page.Layout.get()
		if layout and layout.Content:
			response.out.write(CmsController.RenderPage(page.Content, page))
		else:
			response.out.write(page.Content)
	else:
		response.out.write("404 File Not Found.")

def RenderPage(content, page):
	if content is None:
		content = ""
	page_template = jinja2.Template("{% extends cms__layout_template %}{% block cms__page_content %}" + content + "{% endblock %}")
	return page_template.render(CmsController.GetBaseAndLayoutTemplates(page))

def GetBaseAndLayoutTemplates(page):
	layout = page.Layout.get()
	if layout:
		layout_content = layout.Content
		jinja = jinja2.Environment(loader=JuntaTemplateLoader())
		if "{{SiteMenu}}" in layout.UsedPlaceholders:
			template = jinja.get_template('/admin/cms/special/sitemenu')
			context = { 'pages': CmsPage.query(CmsPage.ParentPage == None).order(CmsPage.Sort) }
			layout_content = layout_content.replace("{{SiteMenu}}", template.render(context))
		if "{{SiblingMenu}}" in layout.UsedPlaceholders:
			template = jinja.get_template('/admin/cms/special/siblingmenu')
			context = { 'pages': CmsPage.query(CmsPage.ParentPage == page.ParentPage).order(CmsPage.Sort) }
			layout_content = layout_content.replace("{{SiblingMenu}}", template.render(context))
		if "{{SignIn}}" in layout.UsedPlaceholders:
			user = users.get_current_user()
			username = "" if not user else user.email()
			context = {'username': username, 'signout_uri': users.create_logout_url(dest_url='/signout'), 'providers': appusers.get_signin_providers()}
			template = jinja.get_template('/admin/cms/special/mini_signin')
			layout_content = layout_content.replace("{{SignIn}}", template.render(context))
		if "{{Content}}" in layout.UsedPlaceholders:
			layout_content = layout_content.replace("{{Content}}", "{% block cms__page_content %}{% endblock %}")

		base_template = jinja.get_template('/admin/cms/special/base')
		layout_template = jinja2.Template("{% extends cms__base_template %}\n{% block cms__layout_body %}" + layout_content + "{% endblock %}")

		return {'cms__base_template': base_template, 'cms__layout_template': layout_template}
	else:
		raise Exception("No layout!")


def GetLayoutTemplate():
	pass

def GetSitemapList():
	depth = 0
	list = []
	CmsController.GetSitemapList_Recursive(list, None, depth)
	return list

def GetSitemapList_Recursive(list, parent, depth):
	pages = CmsPage.query(CmsPage.ParentPage == parent).order(CmsPage.Sort)
	if pages.count() <= 0:
		return
	for page in pages:
		page._depth = depth
		list.append(page)
		CmsController.GetSitemapList_Recursive(list, page.key, depth+1.5)

def GetLayoutList():
	return CmsLayout.query()
