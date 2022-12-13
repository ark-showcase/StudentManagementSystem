from dataclasses import fields
from platform import release
from django import forms
from . import models

class AddressForm(forms.ModelForm):
    class Meta:
        model = models.Address
        fields = "__all__"


class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = "__all__"