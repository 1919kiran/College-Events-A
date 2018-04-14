from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "name",
            "tag",
            "description",
            "date",
            "organiser",
            "contact",
        ]

class NotificationForm(forms.Form):

    subject = forms.CharField(max_length=100)
    body = forms.CharField(required = True, widget=forms.Textarea)
