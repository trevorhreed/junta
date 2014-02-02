from libs import db

_default_values = {
	'Phase1_MaximumProjects':					20,
	'Phase2_MaximumProjects':					10,
	'Phase3_MaximumProjects':					5,
	'Phase4_MaximumProjects':					4,
	'Phase1_MinimumVotes':						100,
	'Phase1_MinimumRatio':						.8,
	'Phase2_MinimumVotes':						100,
	'Phase2_MinimumAvgRating':					.8,
	'Phase3_MinimumVotes':						100,
	'Phase3_MinimumAvgRating':					.8,
	'Phase3_MinimumAvgImpactRating':			.6,
	'Phase3_MinimumAvgInnovationRating':		.6,
	'Phase3_MinimumAvgSustainabilityRating':	.6,
}

def reset_all_to_default():
	for property_id, value in _default_values.items():
		set(property_id, value)

def get(property_id):
	property = SystemProperty.get_by_id(property_id)
	if not property:
		property = SystemProperty(id=property_id)
		property.Value = str(_default_values[property_id])
		property.put()
	return property

def get_value(property_id):
	system_property = get(property_id)
	return system_property.Value

def get_as_int(property_id):
	system_property = get(property_id)
	return int(system_property.Value)

def set(property_id, value):
	value = str(value)
	system_property = SystemProperty.get_by_id(property_id)
	if not system_property:
		system_property = SystemProperty(id=property_id)
	system_property.Value = value
	system_property.put()
	return system_property
