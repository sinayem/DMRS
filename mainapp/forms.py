from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from .models import Register,Reg_marriage, public

class Reg_marriage_Form(forms.ModelForm):
    class Meta:
        model = Reg_marriage
        #fields = ['registration_num','groom_name','groom_nid','bride_name','bride_nid','marriage_date','marriage_fee']
        fields ="__all__"