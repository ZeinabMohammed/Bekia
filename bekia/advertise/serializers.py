from rest_framework import serializers
from .models import Advertise
from django.contrib.auth.models import User

class AdSerializer(serializers.HyperlinkedModelSerializer):
	publisher = serializers.ReadOnlyField(source='publisher.username')
	url 	  = serializers.HyperlinkedIdentityField(view_name='advertise:ad_detailview', source='Advertise')
	class Meta:
		model  = Advertise
		fields = ('url','id','title','publisher','category','description','price','timestamp','approved','location','contact')

class UserSerializer(serializers.HyperlinkedModelSerializer):
	publisher_of = AdSerializer(many=True)
	url 		 = serializers.HyperlinkedIdentityField(view_name='advertise:user-detail', source='User')
	class Meta:
		model  = User
		fields = ('url', 'id','username', 'email', 'publisher_of')
