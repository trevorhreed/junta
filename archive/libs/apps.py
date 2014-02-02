import os
import re
import webapp2
import jinja2
import core

from libs import mdb
from google.appengine.api import users
from libs.views import JuntaTemplateLoader

class BaseApp(webapp2.RequestHandler):
	def _normalize_handler_method(self, method_name):
		return method_name.lower().replace('-', '_').lstrip('_')

	def dispatch(self):
		self.context = {}
		self.jinja = jinja2.Environment(loader=JuntaTemplateLoader())
		if self.is_authenticated() == False:	self.do_unauthenticated()
		if self.is_authorized() == False:		self.do_unauthorized()
		request = self.request
		method_name = request.route.handler_method or self._normalize_handler_method(request.method)
		if method_name == "post" and 'method' in request.POST:
			method_name = self._normalize_handler_method(request.POST['method'])
		method = getattr(self, method_name, None)
		if method is None:
			self.abort(405, headers=[('Allow', '')])
		args, kwargs = request.route_args, request.route_kwargs
		if kwargs:
			args = ()
		try:
			return method(*args, **kwargs)
		except Exception, e:
			return self.handle_exception(e, self.app.debug)

	def render(self, view_or_views):
		if isinstance(view_or_views, str):
			template = self.jinja.get_template(view_or_views)
			self.response.out.write(template.render(self.context))
		elif isinstance(view_or_views, list):
			views = []
			for view in view_or_views:
				template = self.jinja.get_template(view)
				views.append(template.render(self.context))
			self.response.out.write("\n\n\n~~~\n\n\n".join(views))

	def write(self, text):
		self.response.out.write(text)

	def is_authenticated(self):			return True
	def is_authorized(self):			return True
	def do_unauthenticated(self):		pass
	def do_unauthorized(self):			pass
	def start(self):					pass
	def default(self, action):			pass
	def finish(self):					pass

class CmsApp(BaseApp):
	def __init__(self, request, response):
		super(BaseApp, self).__init__(request, response)
		self.PageInfo = CmsPage.query(CmsPage.Path == request.path).get()
		self.user = users.get_current_user()

	def renderCmsApp(self, view):
		if self.PageInfo and self.PageInfo.Layout:
			self.context.update(CmsController.GetBaseAndLayoutTemplates(self.PageInfo))
		template = self.jinja.get_template(view)
		self.response.out.write(template.render(self.context))
