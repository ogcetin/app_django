from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    customer_id = models.IntegerField(default=0, blank=False)
    email = models.CharField(max_length=255, blank=False, unique=True)
    phone = models.CharField(max_length=55)
    auth = models.CharField(max_length=55, blank=False)
    status = models.CharField(max_length=55, blank=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'user'

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=155, blank=False)

    class Meta:
        db_table = 'customer'

class Data(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    name = models.CharField(max_length=155, blank=False)
    phone = models.CharField(max_length=30, blank=False)
    email = models.CharField(max_length=255, blank=False)

    class Meta:
        db_table = 'data'

class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    data_id = models.IntegerField()
    type = models.CharField(max_length=55, blank=False)
    state = models.CharField(max_length=55, blank=False)
    result = models.CharField(max_length=55, blank=False)
    note = models.CharField(max_length=1000, blank=False)

    class Meta:
        db_table = 'activity'

