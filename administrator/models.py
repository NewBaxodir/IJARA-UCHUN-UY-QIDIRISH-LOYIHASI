from django.db import models
from django.contrib.auth.models import AbstractUser
# from multiselectfield import MultiSelectField
from django.db.models.signals import post_save
from django.dispatch import receiver


from django.contrib.auth.models import User


# Foydalanuvchining autentifikatsiyasi
class User(AbstractUser):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)    
    email = models.CharField(max_length=100)
    addd = models.ManyToManyField(to='search.Announcement', related_name='announcement_add', blank=True)
    

    class Meta:
        verbose_name = '1. All users Database'
        verbose_name_plural = '1. All users Database'



 # Moderator yartish kengaytirilgan yordamchi model
class Useradminpage(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    father_name = models.CharField(max_length=60)
    phone_numer = models.CharField(max_length=30)
    pub_date = models.DateTimeField(auto_now_add=True)
    admin_image = models.ImageField(null=True, blank=True, upload_to='images/') 

    def __str__(self):
        return '%s' %(self.user)

    class Meta:
        verbose_name = '1. Useradminpage'
        verbose_name_plural = '1. Useradminpage'



 # Foydalanuvchi yartish kengaytirilgan yordamchi model
class Householder(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_numer = models.CharField(max_length=30)
    pub_date = models.DateTimeField(auto_now_add=True)
    householder_image = models.ImageField(null=True, blank=True, upload_to='images/')


    def __str__(self):
        return '%s' %(self.user)
        
    class Meta:
        verbose_name = '2. Householder'
        verbose_name_plural = '2. Householder'





