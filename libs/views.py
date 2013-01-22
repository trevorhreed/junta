import os
import jinja2
import core

class JuntaTemplateLoader(jinja2.BaseLoader):

	def get_source(self, environment, template):
		self.load_extensions(environment)
		full_path_to_template = core.PATH_VIEWS + template + '.view'
		if not os.path.exists(full_path_to_template):
			raise jinja2.TemplateNotFound("Template file not found: '" + full_path_to_template)
		mtime = os.path.getmtime(full_path_to_template)
		file = open(full_path_to_template)
		source = file.read().decode('utf-8')
		return source, full_path_to_template, lambda: mtime == os.path.getmtime(full_path_to_template)

	def load_extensions(self, environment):
		environment.globals['str'] = str
		environment.globals['len'] = len
