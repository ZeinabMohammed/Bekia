from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from .views import (AdCreate,
					AdDetailView,
					AdUpdateView,
					AdDeleteView,
					category_list,
					# Ad_list,ad_detail,
					# AdListAPI,
					#  AdDetailAPI,
					AdListGeneric,
					AdDetailgeneric,
					UserList,
					UserDetail,
					# api_root,
					# AdViewSet,
					# UserViewSet
					)


app_name="advertise"


urlpatterns= [
	path('new', AdCreate.as_view(), name='create'),
	path('<pk>/detail', AdDetailView.as_view(), name='advertise-detail'),
	path('<pk>/update', AdUpdateView.as_view(), name='advertise-update'),
    path('<pk>/delete', AdDeleteView.as_view(), name='advertise-delete'),
    path('category/', category_list, name='category'),
    #API_URLS:
    # path('list/', Ad_list, name='ad_list'),
    # path('<int:pk>/', ad_detail, name='ad_detail'),
    # path('', include(router.urls)),
    # path('api/', api_root),
    path('listview/', AdListGeneric.as_view(), name ='ad-list'),
    path('detailview/<int:pk>',AdDetailgeneric.as_view(), name ='ad_detailview'),
    path('users/', UserList.as_view(), name ='user-list'),
	path('users/<int:pk>/', UserDetail.as_view(),name ='user-detail'),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
  ]
urlpatterns = format_suffix_patterns(urlpatterns)