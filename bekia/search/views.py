from django.shortcuts import render
from django.views.generic import ListView
from advertise.models import Advertise
from django.db.models import Q
class SearchAdView(ListView):
	model = Advertise
	template_name = "search/view.html"
	def get_queryset(self, *args, **kwargs):
		qs, qs_location = Advertise.objects.all()

		keywords = self.request.GET.get('q', None)
		loc_keywords = self.request.GET.get('p', None)
		if keywords is not None or loc_keywords is not None:
			qs = qs.filter(
						Q(title__icontains=keywords)|
						Q(description__icontains=keywords)|
						Q(price__icontains=keywords)|
						Q(location__icontains=loc_keywords))
			print(qs)
		return qs
def search(request):
	qs = Advertise.objects.filter(approved=True)
	cat = request.GET.get('q', None)
	p = request.GET.get('p', None)
	q_query=Advertise.objects.filter(
						Q(title__icontains=cat)|
						Q(description__icontains=cat)|
						Q(price__icontains=cat))
	p_query = qs.filter(location=p)
	print(cat,p) 
	if cat == None and p == None:
		
		print(qs)
		return render(request,'search/view.html',{"qs":qs})
	elif cat!= None and p==None:
		qs =Advertise.objects.filter(
						Q(title__icontains=cat)|
						Q(description__icontains=cat)|
						Q(price__icontains=cat))
		print(qs)
		return render(request,'search/view.html',{"qs":qs})
		
	elif p != None and cat == None:
		qs = Advertise.objects.filter(location__icontains=p)
		return render(request,'search/view.html',{"qs":qs})
	elif cat!=None and p!=None :
		qs = (Advertise.objects.filter(Q(location__icontains=p))).filter(
																Q(title__icontains=cat)|
																Q(description__icontains=cat)|
																Q(price__icontains=cat)
						)
		print(qs)
	return render(request,'search/view.html',{"qs":qs})