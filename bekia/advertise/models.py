from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
import django_filters
# from pygments.lexers import get_all_lexers
# from pygments.styles import get_all_styles

# LEXERS = [item for item in get_all_lexers() if item[1]]
# LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# STYLE_CHOICES = sorted((item, item) for item in get_all_styles())
CATEGORIES= (
				("Vehicles",'Vehicles'),
				("Properties",'Properties'),
				("MobilePhones&Accessories",'MobilePhones&Accessories'),
				("Electronics&HomeAppliances",'Electronics&HomeAppliances'),
				("Home&Garden",'Home&Garden'),
				("Fashion",'Fashion'),
				("pets",'Pets'),
				("Kids&Babies",'Kids&Babies'),
				("SportingGoods&Bikes",'SportingGoods&Bikes'),
				("Hobbies,Music",'Hobbies,Music'),
				("jobs",'Jobs'),
				("Business&Industrial",'Business&Industrial'),
				("services",'Services'),

            )



class Advertise(models.Model):

	title 		= models.CharField(max_length=120)
	publisher   = models.ForeignKey(User, related_name='publisher_of',null=True, blank=True, on_delete=models.CASCADE)
	category 	= models.CharField(choices=CATEGORIES, max_length=120)
	description = models.TextField(max_length= 200, null=True, blank=True)
	image       = models.ImageField(upload_to='project_static/Advertise/img', null=True, blank=False)
	price       = models.DecimalField(decimal_places=2, max_digits=20)
	timestamp   = models.DateTimeField(auto_now_add=True)
	approved    = models.BooleanField(default=False)
	location    = models.CharField(max_length=120 , null=True, blank=True)
	contact     = models.CharField(max_length=120,null=True, blank=True)

	def __str__(self):
		"""show ad name in admin page"""
		return self.title

	
	def get_absolute_url(self):

		return reverse("advertise:advertise-detail", kwargs={"pk":self.pk})

