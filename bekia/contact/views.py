from django.shortcuts import render,redirect
from .forms import ContactForm
from django.contrib import messages
# Create your views here.
def contact_us(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'Your message was sent succesfully')
			return redirect('/')
	else:
		form = ContactForm()
		messages.error(request, f'please Enter Correct values')
	context = {'form':form}
	return render(request, 'contact.html', context)