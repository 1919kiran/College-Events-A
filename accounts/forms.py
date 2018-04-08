from django.contrib.auth import get_user_model
from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(max_length=32)
    firstname = forms.CharField(max_length=50, required=False)
    lastname = forms.CharField(max_length=50, required=False)
    is_organiser = forms.BooleanField(required=False)
    is_participant = forms.BooleanField(required=False)


    class Meta:
        model = get_user_model() # use this function for swapping user model

    def save(self, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.age = self.cleaned_data['age']
        user.save()
