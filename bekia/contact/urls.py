
from django.urls import path, include

from .views import contact_us
app_name= "contact"

urlpatterns= [
	path('contact/', contact_us , name='contact'),
	]