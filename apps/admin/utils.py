import base64
from libs import mdb
from libs.apps import BaseApp
from libs.cms import CmsPage, CmsLayout
from libs.general import Document
from libs.projects import DevelopmentSector, BudgetRange, Project, ProjectPhases


class SetupApp(BaseApp):

	def get(self):
		self.render('/admin/utils/setup')

	def populate_database(self):
		# dev sectors
		ds1 = DevelopmentSector()
		ds1.Name = "Health"
		ds1.Image = mdb.to_blob(base64.b64decode("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"))
		ds1.ImageMime = "image/png"
		ds1.put()
		ds2 = DevelopmentSector()
		ds2.Name = "Education"
		ds2.Image = mdb.to_blob(base64.b64decode("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"))
		ds2.ImageMime = "image/png"
		ds2.put()

		# budget ranges
		br1 = BudgetRange()
		br1.Name = "Low"
		br1.Min = "$1,000"
		br1.Max = "$9,999"
		br1.put()
		br2 = BudgetRange()
		br2.Name = "Medium"
		br2.Min = "$10,000"
		br2.Max = "$49,000"
		br2.put()
		br3 = BudgetRange()
		br3.Name = "High"
		br3.Min = "$50,000"
		br3.Max = None
		br3.put()

		# layouts
		layout = CmsLayout()
		layout.Name = "Primary Layout"
		layout.Content = """<style type="text/css">.wrapper{margin:0px auto;padding-bottom:5em;width:800px;}.sitemenu{height:30px;font:normal 13px/30px "Arial", Helvetica, sans-serif;padding:0;margin:0;float:right;}.sitemenu li{list-style-type:none;}.sitemenu a{color:#555;}.sitemenu > li{padding:0px 1em;float:left;position:relative;}.sitemenu > li:hover{background-color:#eee;}.sitemenu > li > a{text-decoration:none;}.sitemenu > li > a:hover{text-decoration:none;}	.sitemenu > li > ul{display:none;position:absolute;background-color:#eee;padding:10px;margin-left:-13px;z-index:100;}.sitemenu > li > ul > li{float:none;padding:0;width:150px;text-decoration:none;z-index:100;}.sitemenu > li > ul > li > a{text-decoration:none;}.sitemenu > li > ul > li > a:hover{}.sitemenu > li:hover > ul{display:block;}#mini_signin{float:right;margin-left:1em;font-size:10pt;color:#888;}#mini_signin span{margin-right:.5em;line-height:2em;}</style><div class="wrapper">The Junta Foundation!{{SignIn}}{{SiteMenu}}<div style="clear:both;border-bottom:solid 1px #aaa;"></div>{{Content}}</div>"""
		layout.UsedPlaceHolders = ["{{SiteMenu}}", "{{Content}}"]
		layout.put()

		# pages
		root_page = CmsPage()
		root_page.ParentPage = None
		root_page.Layout = layout.key
		root_page.Type = 1
		root_page.Name = "Junta"
		root_page.Path = "/"
		root_page.Link = "Junta"
		root_page.Sort = "Junta"
		root_page.Enabled = True
		root_page.SiteMenu = True
		root_page.SiblingMenu = True
		root_page.put()

		page1 = CmsPage()
		page1.ParentPage = root_page.key
		page1.Layout = layout.key
		page1.Type = 2
		page1.Name = "Project Vetting"
		page1.Path = "/vetting"
		page1.Link = "Project Vetting"
		page1.Sort = "Project Vetting"
		page1.Enabled = True
		page1.SiteMenu = True
		page1.SiblingMenu = True
		page1.put()

		page2 = CmsPage()
		page2.ParentPage = root_page.key
		page2.Layout = layout.key
		page2.Type = 2
		page2.Name = "Submit Project"
		page2.Path = "/submit"
		page2.Link = "Submit Project"
		page2.Sort = "Submit Project"
		page2.Enabled = True
		page2.SiteMenu = True
		page2.SiblingMenu = True
		page2.put()

		page3 = CmsPage()
		page3.ParentPage = root_page.key
		page3.Layout = layout.key
		page3.Type = 2
		page3.Name = "Past Projects"
		page3.Path = "/past"
		page3.Link = "Past Projects"
		page3.Sort = "Past Projects"
		page3.Enabled = True
		page3.SiteMenu = True
		page3.SiblingMenu = True
		page3.put()

		page4 = CmsPage()
		page4.ParentPage = root_page.key
		page4.Layout = layout.key
		page4.Type = 2
		page4.Name = "Register"
		page4.Path = "/register"
		page4.Link = "Register"
		page4.Sort = "Register"
		page4.Enabled = True
		page4.SiteMenu = True
		page4.SiblingMenu = True
		page4.put()

		page5 = CmsPage()
		page5.ParentPage = root_page.key
		page5.Layout = layout.key
		page5.Type = 2
		page5.Name = "Profile"
		page5.Path = "/profile"
		page5.Link = "Profile"
		page5.Sort = "Profile"
		page5.Enabled = True
		page5.SiteMenu = True
		page5.SiblingMenu = True
		page5.put()

		page6 = CmsPage()
		page6.ParentPage = root_page.key
		page6.Layout = layout.key
		page6.Type = 2
		page6.Name = "Sign In"
		page6.Path = "/signin"
		page6.Link = "Sign In"
		page6.Sort = "Sign In"
		page6.Enabled = True
		page6.SiteMenu = True
		page6.SiblingMenu = True
		page6.put()

		page7 = CmsPage()
		page7.ParentPage = root_page.key
		page7.Layout = layout.key
		page7.Type = 2
		page7.Name = "Library"
		page7.Path = "/library"
		page7.Link = "Library"
		page7.Sort = "Library"
		page7.Enabled = True
		page7.SiteMenu = True
		page7.SiblingMenu = True
		page7.put()

		page8 = CmsPage()
		page8.ParentPage = root_page.key
		page8.Layout = layout.key
		page8.Type = 2
		page8.Name = "Test"
		page8.Path = "/test"
		page8.Link = "Test"
		page8.Sort = "Test"
		page8.Enabled = True
		page8.SiteMenu = True
		page8.SiblingMenu = True
		page8.put()

		# projects

		proj = Project()
		proj.Title = "A Cool Project"
		proj.DevelopmentSector = ds1.key
		proj.Phase = ProjectPhases.Phase1
		proj.Countries = ['Sweden', 'France']
		proj.Image = mdb.to_blob(base64.b64decode("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"))
		proj.ImageMim = "image/png"
		proj.BriefAbstract = "brief"
		proj.LongAbstract = "long"
		proj.HighImpactDescription = "impact"
		proj.SustainabilityDescription = "sustain"
		proj.InnovationDescription = "innovate"
		proj.BudgetDescription = "budget"
		proj.BudgetWorksheet = mdb.to_blob(base64.b64decode("QnVkZ2V0LCwsLCwsLCwNWWVhciwyMDEzLDIwMTQsMjAxNSwyMDE2LDIwMTcsMjAxOCwyMDE5LDIwMjANRXhwZW5zZXMsNTAwLDIwMDAsMTUwMCwxMDAwLDEwMDAsMTAwMCwxMDAwLDEwMDANSW5jb21lLDAsMTAwMCwyMDAwLDUwMDAsNTAwMCw1MDAwLDUwMDAsNTAwMA=="))
		proj.BudgetWorksheetMime = "text/csv"
		proj.BudgetNotes = "none"
		proj.BudgetRange = br1.key
		proj.put()

		# finished:
		self.write("Database populated.")

	def clear_database(self):
		self.write("Not yet implemented.")


class DocumentApp(BaseApp):

	def get(self):
		self.context['docs'] = Document.query()
		self.render('/admin/utils/docs_main')

	def post(self):
		doc = Document()
		doc.stuff(self.request)
		doc.put()
		self.redirect('/admin/utils/docs')

	def rename(self):
		doc_id = self.request.get('doc_id', None)
		new_name = self.request.get('new_name', None)
		if new_name:
			doc = Document.get(doc_id)
			doc.Name = new_name
			doc.put()
		self._renderList()

	def delete(self):
		doc_id = self.request.get('doc_id', None)
		mdb.delete(doc_id)
		self._renderList()

	def _renderList(self):
		self.context['docs'] = Document.query()
		self.render('/admin/utils/docs_list')


class DevSectorApp(BaseApp):

	def get(self):
		self.context['devsectors'] = DevelopmentSector.query()
		self.render('/admin/utils/devsectors_main')

	def post(self):
		devsector = DevelopmentSector()
		devsector.stuff(self.request)
		devsector.put()
		self.redirect('/admin/utils/devsectors')

	def rename(self):
		devsector_id = self.request.get('devsector_id', None)
		new_name = self.request.get('new_name', None)
		if new_name:
			devsector = DevelopmentSector.get(devsector_id)
			devsector.Name = new_name
			devsector.put()
		self.context['devsectors'] = DevelopmentSector.query()
		self.render('/admin/utils/devsectors_list')

	def delete(self):
		devsector_id = self.request.get('devsector_id', None)
		mdb.delete(devsector_id)
		self.context['devsectors'] = DevelopmentSector.query()
		self.render('/admin/utils/devsectors_list')


class BudgetRangeApp(BaseApp):

	def get(self):
		self.context['budgetranges'] = BudgetRange.query().order(BudgetRange.Min)
		self.render('/admin/utils/budgetranges_main')

	def post(self):
		budgetrange = BudgetRange()
		budgetrange.stuff(self.request)
		budgetrange.put()
		self.context['budgetranges'] = BudgetRange.query().order(BudgetRange.Min)
		self.render('/admin/utils/budgetranges_list')

	def rename(self):
		budgetrange_id = self.request.get('budgetrange_id', None)
		new_name = self.request.get('new_name', None)
		if new_name:
			budgetrange = BudgetRange.get(budgetrange_id)
			budgetrange.Name = new_name
			budgetrange.put()
		self.context['budgetranges'] = BudgetRange.query().order(BudgetRange.Min)
		self.render('/admin/utils/budgetranges_list')

	def delete(self):
		budgetrange_id = self.request.get('budgetrange_id', None)
		mdb.delete(budgetrange_id)
		self.context['budgetranges'] = BudgetRange.query().order(BudgetRange.Min)
		self.render('/admin/utils/budgetranges_list')
