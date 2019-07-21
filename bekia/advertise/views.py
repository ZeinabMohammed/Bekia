from django.shortcuts import render
from .forms import AdForm
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Advertise
from django.db.models import Q
from django.http import HttpResponse,JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.reverse import reverse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status,mixins,generics,viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from advertise.serializers import AdSerializer,UserSerializer
class AdCreate(LoginRequiredMixin, CreateView):
	model = Advertise
	fields = [
			'title',
			'category',
			'description',
			'image',
			'price',
			'location',
			'contact',
					]
	def form_valid(self, form):
		form.instance.publisher=self.request.user
		return super().form_valid(form)

	def test_func(self):
		Ad = self.get_object()
		if request.user == Ad.user:
			return True
		return False
	def perform_create(self, serializer):
		serializer.save(publisher=self.request.user)

class AdDetailView(DetailView):
	model = Advertise
	template_name = 'advertise/advertise_detail.html'


class AdUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
	model = Advertise
	fields = fields = [
			'title',
			'category',
			'description',
			'image',
			'price',
			'location',
			'contact',
					]
	def test_func(self):
		ad = self.get_object()
		if self.request.user == ad.publisher:
			return True
		return False

	def form_valid(self, form):
		form.instance.publisher = self.request.user
		return super().form_valid(form)

class AdDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Advertise
	success_url = '/'
	def test_func(self):
		ad= self.get_object()
		if self.request.user == ad.publisher:
			return True
		return False
# class CategoryView(ListView):
# 	model = Advertise
# 	template_name = "advertise/category.html"
# 	def get_queryset(self, *args, **kwargs):
# 		qs = Advertise.objects.all()
# 		keywords = self.request.GET.get('q', None)
# 		if keywords is not None:
# 			qs = qs.filter(
# 						Q(category=keywords))
# 		return qs

def category_list(request):
	cat = request.GET.get('q', None)
	if cat == None:
		return render(request, 'index.html')
	else:
		qs = Advertise.objects.all().filter(Q(category=cat)|
											Q(title__icontains=cat)|
											Q(description__icontains=cat)|
											Q(price__icontains=cat))
		print(qs)
		return render(request,'advertise/category.html',{"qs":qs})


#API Views:
#*************************************************************************************#
# @permission_classes([permissions.IsAuthenticatedOrReadOnly], [IsOwnerOrReadOnly],)
class AdListGeneric(generics.ListCreateAPIView):
	permission_classes=(permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
	queryset=Advertise.objects.all()
	serializer_class=AdSerializer

# @permission_classes([permissions.IsAuthenticatedOrReadOnly],[IsOwnerOrReadOnly])
class AdDetailgeneric(generics.RetrieveUpdateDestroyAPIView):
	permission_classes=(permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
	queryset=Advertise.objects.all()
	serializer_class=AdSerializer

# #userapi views:
# @permission_classes([permissions.IsAuthenticatedOrReadOnly])
class UserList(generics.ListAPIView):
	permission_classes=(permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
	queryset=User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	permission_classes=(permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
	queryset = User.objects.all()
	serializer_class = UserSerializer

# #create endpoint for root of API:	
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly])
def api_root(request, format=None):
	return Response({
					 'users': reverse('advertise:user-list', request=request, format=format),
					 'advertise':reverse("advertise:ad-list", request=request, format=format)
					})
#Function BV:

# @api_view(['GET', 'POST'])
# @permission_classes([permissions.IsAuthenticatedOrReadOnly])
# def Ad_list(request, format=None):
# 	"""list all advertises or create new advertise"""
# 	if request.method == 'GET':
# 		queryset = Advertise.objects.all()
# 		serializer = AdSerializer(queryset, many=True)
# 		return Response(serializer.data)
# 	elif request.method == 'POST':
# 		queryset = Advertise.objects.all()
# 		serializer = AdSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([permissions.IsAuthenticatedOrReadOnly])
# def ad_detail(request,pk, format=None):
# 	"""RUD"""
# 	try:
# 		ad = Advertise.objects.get(pk=pk)
# 	except Advertise.DoesNotExist:
# 		return HttpResponse(status=status.HTTP_404_NOT_FOUND)
# 	if request.method == 'GET':
# 		serializer = AdSerializer(ad)
# 		return Response(serializer.data)
# 	elif request.method == 'PUT':
# 		serializer = AdSerializer(ad, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 	elif request.method == 'DELETE':
# 		ad.delete()
# 		return HttpResponse(status=status.HTTP_204_NO_CONTENT)
#CBV:
# @permission_classes((permissions.AllowAny,IsOwnerOrReadOnly))
# class AdListAPI(APIView):
# 	"""list all ads or create new one"""
# 	def get(self, request, format=None):
# 		ads=Advertise.objects.all()
# 		serializer =AdSerializer(ads, many=True)
# 		return Response(serializer.data)

# 	def post(self,request, format=None):
# 		serializer=AdSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # @permission_classes([permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly])
# class AdDetailAPI(APIView):
# 	"""RUD"""
# 	permission_classes=(permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
# 	def get_object(self,pk):
# 		try:
# 			return Advertise.objects.get(pk=pk)
# 		except Advertise.DoesNotExist:
# 			raise Http404
# 	def get(self, request,pk, format=None):
# 		Ad = self.get_object(pk)
# 		serializer = AdSerializer(Ad,context={'request': request})
# 		return Response(serializer.data)
# 	def put(self, request,pk, format=None):
# 		Ad = self.get_object(pk)
# 		serializer = AdSerializer(Ad, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 	def delete(self, request, pk, format=None):
# 		Ad = self.get_object(pk)
# 		Ad.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)
#using mixins
# class AdListMixin(mixins.ListModelMixin,
# 				  mixins.CreateModelMixin,
# 				  generics.GenericAPIView):
# 	queryset = Advertise.objects.all()
# 	serializer_class=AdSerializer

# 	def get(self,request,*args, **kwargs):
# 		return self.list(request, *args, **kwargs)
# 	def post(self, request, *args, **kwargs):
# 		return self.create(request,*args,**kwargs)
# class AdDetailMixin(mixins.RetrieveModelMixin,
# 					mixins.UpdateModelMixin,
# 					mixins.DestroyModelMixin,
# 					generics.GenericAPIView):
# 	queryset = Advertise.objects.all()
# 	serializer_class = AdSerializer

# 	def get(self, request, *args, **kwargs):
# 		return self.retrieve(requset, *args, **kwargs)

# 	def put(self, request, *args, **kwargs):
# 		return self.update(requset, *args, **kwargs)

# 	def delete(self, request, *args, **kwargs):
# 		return self.destroy(requset, *args, **kwargs)


# using generic CBVs:


# #userapi views:
# @permission_classes([permissions.IsAuthenticatedOrReadOnly])
# class UserList(generics.ListAPIView):
# 	queryset=User.objects.all()
# 	serializer_class = UserSerializer

# class UserDetail(generics.RetrieveAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer

# #create endpoint for root of API:

# class AdViewSet(viewsets.ReadOnlyModelViewSet):
# 	"""
# 	automatically provides 'list' and 'detail' views
# 	"""
# 	permission_classes=(permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
# 	queryset = Advertise.objects.all()
# 	serializer_class = AdSerializer
# class UserViewSet(viewsets.ReadOnlyModelViewSet):
# 	"""
# 	automatically provides 'list' and 'detail' views
# 	"""
# 	permission_classes=(permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer