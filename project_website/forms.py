
from django import forms

class UserForm(forms.Form):
    firstname = forms.CharField(required=True, label="First Name",max_length=100)
    lastname = forms.CharField(required=True, label="Last Name",max_length=100)
    r_name = forms.CharField(required=True, label="Restaurant / Company Name",max_length=100)
    r_number = forms.CharField(required=True, label="Restaurant / Company Phone Number",max_length=100, widget=forms.TextInput(attrs={'placeholder': 'XXX-XXX-XXXX'}))
    r_address = forms.CharField(required=True, label="Restaurant / Company Address",max_length=100)
    phone = forms.CharField(required=True, label="Cell Phone",max_length=100, widget=forms.TextInput(attrs={'placeholder': 'XXX-XXX-XXXX'}))
    email = forms.EmailField(required=True, )