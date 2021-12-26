from django import forms

class NameForm(forms.Form):
    username = forms.CharField(label='your_name', max_length=100)
    password = forms.CharField(label = 'your_passowrd', max_length= 100)
    email = forms.CharField(label = 'your_email', max_length= 100)
    is_farmer = forms.BooleanField(label = 'is_farmer')