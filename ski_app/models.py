from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	items = models.IntegerField(default=0)

	def __unicode__(self):
		return self.name

class Ski_Page(models.Model):
	category = models.ForeignKey(Category)
	model_name = models.CharField(max_length=128, unique=True)
	brand = models.CharField(max_length=128, choices=(("Rosignol", "Rosignol"), ("RosZZ", "RosZZ"), ("KosZZ", "KosZZ")))
	skier_level = models.IntegerField()
	intended_usage = models.CharField(max_length=128)
	profile = models.CharField(max_length=128)
	rocker_ratio = models.IntegerField() 
	turn_radius = models.DecimalField(max_digits=3,decimal_places=1)
	tip_width = models.IntegerField()
	waist_width = models.IntegerField()
	tail_width = models.IntegerField()
	core_material = models.CharField(max_length=128)
	reinforcement_material = models.CharField(max_length=128)
	weight = models.DecimalField(max_digits=3,decimal_places=1)
	womens = models.CharField(max_length=128)
	ski_length = models.CommaSeparatedIntegerField(max_length=128)
	ref_length = models.IntegerField()
	rating = models.FloatField()
	picture = models.ImageField(upload_to='ski_images',blank=True)
	description = models.TextField()
	powder_award = models.CharField(max_length=128)
	ski_award = models.CharField(max_length=128)
	skiing_award = models.CharField(max_length=128)
	freeskier_award = models.CharField(max_length=128)
	backcountry_award = models.CharField(max_length=128)

	def __unicode__(self):
		return self.model_name

class UserProfile(models.Model):
	user = models.OneToOneField(User)

	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)

	def __unicode__(self):
		return self.user.username
