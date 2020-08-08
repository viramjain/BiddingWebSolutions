from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE
# Create your models here.
class SignUp(models.Model):
    user=models.ForeignKey(to=User,on_delete=CASCADE,null=True)
    contact_num=models.CharField(max_length=15)
    address=models.TextField()
    city=models.CharField(max_length=20)
    pincode=models.CharField(max_length=15)
    gender=models.CharField(max_length=10)
    def __str__(self):
         return self.user


