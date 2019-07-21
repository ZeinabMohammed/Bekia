from django.db import models


class ContactUs(models.Model):
	name 	= models.CharField(max_length=120, null=True, blank=True)
	email 	= models.EmailField(null=True, blank=True)
	subject = models.CharField(max_length=120,null=True, blank=True)
	message = models.TextField(max_length=300,null=True, blank=True)
	

	def __str__(self):
		return self.name


	class Meta:
		verbose_name_plural = "contact us"