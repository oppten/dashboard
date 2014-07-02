from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'jsDashboard/index.html')

def detail(request, dboard_id):
	context = {'dboard_id': dboard_id}
	template = 'jsDashboard/'+ dboard_id +'.html'
	return render(request, template, context)
