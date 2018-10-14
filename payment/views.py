from django.shortcuts import render

# Create your views here.
def home(request, pk=None, *args, **kwargs):
	context = {}
	return render(request, 'payment/home.html', context)