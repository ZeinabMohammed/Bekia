from django import forms
from .models import Advertise
class AdForm(forms.ModelForm):
	class Meta:
		model  = Advertise
		fields = [
					'title',
					'category',
					'description',
					'image',
					'price',
				
					]


