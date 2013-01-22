from libs import sysprops, apps

class TrusteeVettingApp(apps.BaseApp):
	def get(self):
		self.context['Phase1_MaximumProjects']					= sysprops.get_value('Phase1_MaximumProjects')
		self.context['Phase2_MaximumProjects']					= sysprops.get_value('Phase2_MaximumProjects')
		self.context['Phase3_MaximumProjects']					= sysprops.get_value('Phase3_MaximumProjects')
		self.context['Phase4_MaximumProjects']					= sysprops.get_value('Phase4_MaximumProjects')
		self.context['Phase1_MinimumVotes']						= sysprops.get_value('Phase1_MinimumVotes')
		self.context['Phase1_MinimumRatio']						= sysprops.get_value('Phase1_MinimumRatio')
		self.context['Phase2_MinimumVotes']						= sysprops.get_value('Phase2_MinimumVotes')
		self.context['Phase2_MinimumAvgRating']					= sysprops.get_value('Phase2_MinimumAvgRating')
		self.context['Phase3_MinimumVotes']						= sysprops.get_value('Phase3_MinimumVotes')
		self.context['Phase3_MinimumAvgRating']					= sysprops.get_value('Phase3_MinimumAvgRating')
		self.context['Phase3_MinimumAvgImpactRating']			= sysprops.get_value('Phase3_MinimumAvgImpactRating')
		self.context['Phase3_MinimumAvgInnovationRating']		= sysprops.get_value('Phase3_MinimumAvgInnovationRating')
		self.context['Phase3_MinimumAvgSustainabilityRating']	= sysprops.get_value('Phase3_MinimumAvgSustainabilityRating')

		self.render('/admin/trustees/vetting_main')

	def update_system_property(self):
		property_name = self.request.get('property_name', None)
		property_value = self.request.get('property_value', None)
		if property_name and property_value:
			sysprops.set(property_name, property_value)

	def reset_all_system_properties(self):
		sysprops.reset_all_to_default()
