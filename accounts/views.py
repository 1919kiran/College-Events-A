from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')

def contact(request):
    return render(request, 'accounts/contact.html', {})

def events_redirect(request):
    return redirect('events:index')
