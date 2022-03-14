from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.http import request
from django.utils import timezone

class Register(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='reg')
    name = models.CharField(max_length=500)
    nid = models.BigIntegerField(primary_key=True)
    phone = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    #logo = models.ImageField(upload_to='restaurant_logo/', blank=False)

    def __str__(self):
        return self.name

class public(models.Model):
    name = models.CharField(max_length=500)
    ch= (
    ('male', 'male'),
    ('female', 'female'),
    )
    gender = models.CharField(max_length=50,choices=ch)
    nid = models.BigIntegerField(primary_key=True,null=False)
    #status = models.IntegerField(choices = STATUS_CHOICES)
    #avatar = models.CharField(max_length=500)
    phone = models.CharField(max_length=500, blank=True)
    address = models.CharField(max_length=500, blank=True)
    STATUS_CHOICES = (
    ('married', 'married'),
    ('unmarried', 'unmarried'),
    )
    status = models.CharField(max_length=50,choices=STATUS_CHOICES)
    
    def __str__(self):
        return str(self.nid)

class Reg_marriage(models.Model):
    registration_num = models.IntegerField(primary_key=True)
    groom_name = models.CharField(max_length=200)
    groom_nid = models.OneToOneField(
        public, on_delete=models.CASCADE, related_name="g_nid"
    )
    bride_name = models.CharField(max_length=200)
    bride_nid = models.OneToOneField(
        public, on_delete=models.CASCADE, related_name="b_nid"
    )
    marriage_date = models.DateTimeField(default = timezone.now)
    marriage_fee = models.FloatField()

    def __str__(self):
        return str(self.registration_num)
    # registration_num = models.IntegerField(primary_key=True, unique=True)
    # reg = models.OneToOneField(Register, on_delete=models.CASCADE, related_name='reg')
    # groom_name = models.CharField(max_length=500)
    # groom_nid = models.BigIntegerField()
    # bride_name = models.CharField(max_length=500)
    # bride_nid = models.BigIntegerField()
    # short_description = models.CharField(max_length=500)
    # #image = models.ImageField(upload_to='meal_images/', blank=False)
    # fee = models.IntegerField(default=0)
    # created_at = models.DateTimeField(default = timezone.now)


    # def __str__(self):  
    #     return self.registration_num