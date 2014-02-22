import os

def populate():
	ski_cat = add_cat('Skis')

	boot_cat = add_cat("Boots")

	for c in Category.objects.all():
		for p in Ski_Page.objects.filter(category=c):
			print "- {0} - {1}".format(str(c),str(p))


def add_cat(name):
	c = Category.objects.get_or_create(name=name)[0]
	return c

if __name__ == '__main__':
	print "Starting ski_app population script..."
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ski_project.settings')
	from ski_app.models import Category, Ski_Page
	populate()
