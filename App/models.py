from django.db import models

class UserData(models.Model):
    Username = models.TextField(max_length=50, blank=True)
    Name = models.TextField(max_length=50, blank=True)
    Description = models.TextField(max_length=50, blank=True)
    Photos = models.TextField(max_length=50, blank=True)
    Location = models.TextField(max_length=50, blank=True)
    Sex = models.TextField(max_length=50, blank=True)
    SexWant = models.TextField(max_length=50, blank=True)
    RadiusWant = models.IntegerField(max_length=50, blank=True)





