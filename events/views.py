from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event
from .forms import EventForm

# Create your views here.
def about(request):
    return render(request, 'events/about.html')

def detail(request, slug):
    event = get_object_or_404(Event, tag=slug)
    return render(request, 'events/detail.html', {'event':event})

#Creating an event
@login_required
def create(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #messages.success(request, "Event Created") #It is not rendered as it was not fitting with the template
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        pass
        #messages.error(request, "Could not create Event")
    return render(request, 'events/createform.html', {'form': form})

#Updating an event
@login_required
def update(request, slug=None):
    event = Event.objects.get(tag=slug) #checking if logged in user is the organiser of the event
    organiser_of_event = event.organiser
    instance = get_object_or_404(Event, tag=slug)
    form = EventForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #messages.success(request, "Event details updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        return render(request, 'events/about.html')
        #messages.error(request, "Could not update Event")

    context = {
        'name' : instance.name,
        'description' : instance.description,
        'date' : instance.date,
        'organiser' : instance.organiser,
        'contact' : instance.contact,
        'form' : form,
        'organiser_of_event' : organiser_of_event,
    }
    return render(request, 'events/updateform.html', context)

@login_required
def delete(request, slug=None):
    event = Event.objects.get(tag=slug)
    organiser_of_event = event.organiser
    if request.user == organiser_of_event:
        instance = get_object_or_404(Event, tag=slug)
        instance.delete()
        messages.success(request, "Event deleted")
        return redirect('events:index')
    else:
        return render(request, 'events/delete.html')

def index(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'events/index.html', {'event_list': events})

def home(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'events/index.html', {'event_list': events})
