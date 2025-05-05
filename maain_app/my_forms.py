from django import forms

from maain_app.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['names', 'email', 'phone', 'password', 'weight', 'height', 'gender']