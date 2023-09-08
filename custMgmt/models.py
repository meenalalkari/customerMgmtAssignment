from django.db import models

# Create your models here.
class Customer(models.Model):
    GENDER = [('F', 'female'), ('M', 'male')]
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    mobile = models.IntegerField()
    email = models.EmailField()
    gender = models.CharField(choices=GENDER, max_length=20, default='f')
