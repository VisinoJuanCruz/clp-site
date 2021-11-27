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

class Agent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this setup')
    name = models.CharField(max_length=20, help_text="Enter a agent name")
    rol = models.ForeignKey('Rol',on_delete=models.SET_NULL, null=True, help_text="Select a rol for this Agent")
    def __str__(self):
        return self.name



class Player(Person):
    nick = models.CharField(max_length=25, help_text="Enter a player nick")
    played_hours = models.IntegerField()
    rank = models.ForeignKey('Rank', on_delete=models.SET_NULL, blank= True, null=True) 
    agents = models.ManyToManyField('Agent',help_text="Enter a agents", blank=True)

    sensivility = models.FloatField(help_text="Enter a sens number",blank= True,null=True)
    dpi = models.IntegerField(help_text="Enter a dpi number",blank= True, null=True)

    monitor = models.CharField(max_length=50, help_text="Enter a monitor name",blank= True, null=True)
    mouse = models.CharField(max_length=50, help_text="Enter a mouse name",blank= True, null=True)
    mousepad = models.CharField(max_length=50, help_text="Enter a mousepad name",blank= True, null=True)
    keyboard = models.CharField(max_length=50, help_text="Enter a keyboard name",blank= True, null=True)
    headset = models.CharField(max_length=50, help_text="Enter a headset name",blank= True, null=True)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Player._meta.fields]


    def __str__(self):
        return self.nick
   
    def get_absolute_url(self):
        return reverse('player-detail',args=[str(self.id)])

class Rank(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this rank')
    name = models.CharField(max_length=20, help_text="Enter a rank name")

    def __str__(self):
        return self.name

class Map(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this map')
    name = models.CharField(max_length=20, help_text="Enter a map name")

    def __str__(self):
        return self.name


class Rol(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this setup')
    name = models.CharField(max_length=20,help_text="Enter a rol name")
    def __str__(self):
        return self.name

