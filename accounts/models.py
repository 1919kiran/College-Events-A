from django.db import models

class User(models.Model):
    username = models.CharField(max_length=32)
    firstname = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50, null=True)
    is_organiser = models.BooleanField(default=False)
    is_participant = models.BooleanField(default=True)

    def __str__(self):
        if not str(self.firstname + ' ' + self.lastname):
            return str(self.firstname + ' ' + self.lastname)
        else:
            return self.username
