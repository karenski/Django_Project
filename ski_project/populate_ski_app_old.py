import os

def populate():
	ski_cat = add_cat('Skis')

	add_ski(cat=ski_cat,
		model_name = 'Soul 7',
		brand = 'Rossignol',
		skier_level = '2',
		intended_usage = 'Mixed',
		profile = 'Mustache',
		rocker_ratio = '65',
		turn_radius = '17',
		tip_width = '136',
		waist_width = '106',
		tail_width = '126',
		core_material = 'Paulownia',
		reinforcement_material = 'N/A',
		weight = '9.0',
		womens = 'no',
		ski_length = '164, 172, 180, 188',
		ref_length = '180',
		description = 'N/A')

	add_ski(cat=ski_cat,
		model_name = 'Mantra',
		brand = 'Volkl',
		skier_level = '3',
		intended_usage = 'Groomed',
		profile = 'Tip',
		rocker_ratio = '80',
		turn_radius = '24.2',
		tip_width = '132',
		waist_width = '98',
		tail_width = '118',
		core_material = 'Sensorwood',
		reinforcement_material = 'Metal',
		weight = '10.5',
		womens = 'no',
		ski_length = '170, 177, 184, 191',
		ref_length = '184',
		description = 'N/A')

	add_ski(cat=ski_cat,
		model_name = 'Bibby Pro',
		brand = 'Moment',
		skier_level = '3',
		intended_usage = 'Powder',
		profile = 'Mustache',
		rocker_ratio = '68',
		turn_radius = '20',
		tip_width = '145',
		waist_width = '120',
		tail_width = '136',
		core_material = 'Aspen/pine',
		reinforcement_material = 'Fiberglass/carbon fiber',
		weight = '10.0',
		womens = 'no',
		ski_length = '176, 186, 192',
		ref_length = '186',
		description = 'N/A')

	boot_cat = add_cat("Boots")

	for c in Category.objects.all():
		for p in Ski_Page.objects.filter(category=c):
			print "- {0} - {1}".format(str(c),str(p))

def add_ski(cat, model_name, brand, skier_level, intended_usage, profile, rocker_ratio, turn_radius, tip_width, waist_width, tail_width, core_material, reinforcement_material, weight, womens, ski_length, ref_length, description):
	p = Ski_Page.objects.get_or_create(category=cat, model_name = model_name, brand = brand, skier_level = skier_level, intended_usage = intended_usage, profile = profile, rocker_ratio = rocker_ratio, turn_radius = turn_radius, tip_width = tip_width, waist_width = waist_width, tail_width = tail_width, core_material = core_material, reinforcement_material = reinforcement_material, weight = weight, womens = womens, ski_length = ski_length, ref_length = ref_length, description = description)[0]
	return p

def add_cat(name):
	c = Category.objects.get_or_create(name=name)[0]
	return c

if __name__ == '__main__':
	print "Starting ski_app population script..."
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ski_project.settings')
	from ski_app.models import Category, Ski_Page
	populate()
