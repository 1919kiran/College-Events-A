from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from django.contrib import messages
from .models import Event
from .forms import EventForm

# Create your views here.
def about(request):
    return render(request, 'about.html')

def detail(request, slug):
    event = get_object_or_404(Event, tag=slug)
    #return HttpResponse(event.name + event.tag + event.description)
    return render(request, 'detail.html', {'event':event})

#Creating an event
def create(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Event Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Could not create Event")
    return render(request, 'createform.html', {'form': form})

#Updating an event
def update(request, slug=None):
    instance = get_object_or_404(Event, tag=slug)
    form = EventForm(request.POST or None, instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Event details updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Could not update Event")

    context = {
        'name' : instance.name,
        'description' : instance.description,
        'date' : instance.date,
        'organiser' : instance.organiser,
        'contact' : instance.contact,
        'form' : form
    }
    return render(request, 'updateform.html', context)

def delete(request, slug=None):
    instance = get_object_or_404(Event, tag=slug)
    instance.delete()
    messages.success(request, "Event deleted")
    return redirect('events:index')

def forum(request):
    return render(request, 'events/forum.html')

def index(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'events/index.html', {'event_list': events})

def home(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'events/index.html', {'event_list': events})

def contact(request):
    return render(request, 'events/contact.html')
