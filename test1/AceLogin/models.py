

# Create your models here.
from enum import unique
from django.db import models
# Create your models here.
from django.contrib.auth import get_user_model

from phonenumber_field.modelfields import PhoneNumberField
from .validators import validate_file



User= get_user_model()
TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]
class RegisterUser(models.Model):
    firstName = models.CharField(max_length = 100)
    lastName = models.CharField(max_length = 100, null= True)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES, null=False,default='MR')
    phoneNumber = PhoneNumberField(unique=False,null = False)
    email = models.EmailField('email', null=True, blank=True)

    password= models.TextField()
    
   
   
    def __str__(self):
        return self.firstName

class Book(models.Model):
    name=models.CharField(max_length=100,
    #default
    default="."
    )
    resume= models.FileField(blank=True,verbose_name="", validators=[validate_file]) 
    linkedin=models.URLField(max_length=200, blank=True,
    #default
    default=""
    )
    def __str__(self):
        return self.name
    
