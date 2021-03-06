from django.db import models
from geopy.geocoders import GoogleV3
# Create your models here.
class Shelter(models.Model):
    Name = models.CharField(max_length=200,default="")
    Address = models.CharField(max_length=100);
    Phone = models.CharField(max_length=100);
    Email = models.EmailField(max_length=100);
    Description = models.CharField(max_length=100,blank = True);
    maxCap = models.IntegerField(default = 0);
    currCap = models.IntegerField(default = 0);
    place_id = models.CharField(max_length=40)
    foodAvailable = models.NullBooleanField()
    shelterAvailable = models.NullBooleanField()
    hygenicAvailable = models.NullBooleanField()
    counselingAvailable = models.NullBooleanField()
    otherDetails = models.CharField(max_length=500,blank=True)
    latitude = models.DecimalField(max_digits=9,decimal_places=6)
    longitude = models.DecimalField(max_digits=9,decimal_places=6)

    def __str__(self):
        return self.Name

class Request(models.Model):
    Address = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9,decimal_places=6)
    longitude = models.DecimalField(max_digits=9,decimal_places=6)
    Time = models.DateTimeField('date published');

def MakeShelter(Values):
    s = Shelter()
    s.Name = Values['Name'];
    s.Address = Values['Address']
    s.Phone = Values['Contact']
    s.Email = Values['ContactE']
    
    if 'Description' in Values:
        s.Description = Values['Description']
    s.currCap = Values['currCap']
    if 'maxCap' in Values:
        s.maxCap = Values['maxCap']
        
    s.foodAvailable = 'foodAvailable' in Values
    
    s.shelterAvailable = 'shelterAvailable' in Values
    
    if s.shelterAvailable and 'maxCap' not in Values:
        return False

    s.hygenicAvailable = 'hygenicAvailable' in Values

    s.counselingAvailable = 'counselingAvailable' in Values
    
    if 'otherDetails' in  Values:
        s.otherDetails = Values['otherDetails']
    
                                
    g = GoogleV3()
    g = g.geocode(s.Address)
    s.latitude = g.latitude
    s.longitude = g.longitude
    s.place_id = g.raw['place_id']
    s.save();
    return True
