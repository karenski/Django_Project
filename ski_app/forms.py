from django import forms
from ski_app.models import Ski_Page, UserProfile
from django.contrib.auth.models import User

class SkiForm(forms.ModelForm):
	model_name = forms.CharField(max_length=128, help_text = "Model name:")
	# brand = forms.CharField(max_length=128, help_text = "Brand name:")
	skier_level = forms.CharField(max_length=128, help_text = "Skier level:") 
	intended_usage = forms.CharField(max_length=128, help_text = "Recommended Usage:")
	profile = forms.CharField(max_length=128, help_text = "Rocker Profile:")
	rocker_ratio = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
	turn_radius = forms.DecimalField(max_digits=3,decimal_places=1, help_text = "Turn radius (m):")
	tail_width = forms.IntegerField(help_text = "Tip width (mm):")
	waist_width = forms.IntegerField(help_text = "Waist width (mm):")
	tail_width = forms.IntegerField(help_text = "Tail width (mm):")
	core_material = forms.CharField(max_length=128, help_text = "Core Material:")
	reinforcement_material = forms.CharField(max_length=128, help_text = "Reinforcement Material:")
	weight = forms.DecimalField(max_digits=3,decimal_places=1, widget=forms.HiddenInput(), help_text = "Weight:")
	womens = forms.CharField(max_length=128, widget=forms.HiddenInput(), help_text = "Women's Specific (Yes/No):")
	ski_length = forms.IntegerField(widget=forms.HiddenInput(),help_text = "Available Lengths(cm):")
	ref_length = forms.IntegerField(widget=forms.HiddenInput(),help_text = "Reference Length (cm):")
	picture = forms.ImageField(help_text="Select an image to upload.", required=False)
	rating = forms.FloatField(widget=forms.HiddenInput(),initial=0)


	class Meta:
		model = Ski_Page
		fields = ('model_name', 'brand', 'skier_level', 'intended_usage', 'profile', 'turn_radius', 'tip_width', 'waist_width', 'tail_width', 'core_material', 'reinforcement_material', 'picture')


class SkiSearchForm(forms.Form):
	brand = forms.ChoiceField(required=False, choices=(('','All'),("Rossignol", "Rossignol"), ("Armada", "Armada"), ("Atomic", "Atomic"), ("Volkl", "Volkl"), ("Blizzard", "Blizzard")))
	intended_usage = forms.ChoiceField(required=False, choices=(('','All'),('Pow', 'Pow'), ('All_Mountain_Pow', 'All_Mountain_Pow'), ('All_Mountain', 'All_Mountain'), ('Frontsider', 'Frontsider'), ('All_Mountain_Carve', 'All_Mountain_Carve'), ('Big_Pow', 'Big_Pow')))
	reinforcement_material = forms.ChoiceField(required=False, choices=(('','All'),('Bamboo', 'Bamboo'), ('Titanium', 'Titanium'), ('None', 'None'), ('Wood', 'Wood')))


class UserForm(forms.ModelForm):
	username = forms.CharField(help_text="Please enter a username.")
	email = forms.CharField(help_text="Please enter your email address.")
	password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password.")

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	website = forms.URLField(help_text="Please enter your website.", required=False)
	picture = forms.ImageField(help_text="Select a profile image to upload.", required=False)
	
	class Meta:
		model = UserProfile
		fields = ('website','picture')


