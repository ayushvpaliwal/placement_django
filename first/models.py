from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone



class placement(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length = 254)
    phone = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class language(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length = 254)
    phone = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    
class algorithm(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length = 254)
    phone = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    
class development(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length = 254)
    phone = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    
class enquiry(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length = 254)
    message= models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    


