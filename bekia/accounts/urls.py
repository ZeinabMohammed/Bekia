from django.urls import path, include
from rest_framework import routers
from accounts import views

# router = routers.DefaultRouter()
# router.register('users', views.UserViewSet)
# router.register('groups', views.GroupViewSet)


urlpatterns=[
	path('', include('registration.backends.default.urls')),
	# path('', include(router.urls)),
	#add login in API page
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    # path('userslist', views.UserList.as_view(), name='userlist'),
    # path('user/<int:pk>', views.UserDetail.as_view(), name='userdetail'),
]
	

