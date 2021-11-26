from django.db import models
from django.urls import reverse
import uuid


class Country(models.Model):
    id= models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this country')
    name = models.CharField(max_length=200,help_text="Enter a country name")

    def __str__(self):
        return self.name

class Person(models.Model):
    id= models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this person')
    fullname= models.CharField(max_length=30, help_text="Enter a player fullname")
    birthday= models.DateField  (null=True, blank=True)
    country= models.ForeignKey('Country', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.fullname

class Player(Person):
    nick = models.CharField(max_length=25, help_text="Enter a player nick")
    played_hours = models.IntegerField()
    rank = models.ForeignKey('Rank', on_delete=models.SET_NULL, null=True) 
    def __str__(self):
        return self.nick
   
    def get_absolute_url(self):
        return reverse('player-detail',args=[str(self.id)])

class Rank(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this rank')
    name = models.CharField(max_length=20, help_text="Enter a rank name")

    def __str__(self):
        return self.name
