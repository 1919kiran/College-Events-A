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

    name = forms.CharField(required = True, max_length=120)
    subject = forms.CharField(required = True, widget=forms.Textarea)
    body = forms.CharField(required = True, widget=forms.Textarea)
