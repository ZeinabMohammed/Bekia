from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from advertise.models import Advertise
from django.db.models import Q

def index(request):
	qs = Advertise.objects.filter(approved=True)
	q = request.GET.get('q', None)
	print(q) 
	if q == None:
		return render(request, 'index.html', {'qs':qs})
	else:
		qs = Advertise.objects.filter(category__icontains=q)
		return render(request,'advertise/category.html',{"qs":qs})
	



@login_required
def profile(request):

	user = User.objects.get(id=request.user.id)
	if request.method =='POST':
		u_form = UserUpdateForm(request.POST,instance=request.user)
		
		if u_form.is_valid() :
			u_form.save()
		
		messages.success(request, f'Yout Account successfully Updated')
		return redirect('/')
	else:
		u_form = UserUpdateForm(instance=request.user)
		
	context={
			'user_update': u_form,
			
			}
	return render(request, 'profile.html', context)

def about(request):
	return render(request, 'about.html')
def safety(request):
	return render(request, 'safety.html')
def terms(request):
	return render(request, 'terms.html')