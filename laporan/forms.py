from django import forms
from curhat import models

class laporanForm(forms.Form):

    name = forms.CharField(
        label = "Informer Name",
        max_length= 60,
        required= True,
        widget = forms.TextInput(attrs = {'class' : 'input', 'placeholder' : 'Name'})
    )

    phone_num = forms.CharField(
        label = "Phone Number",
        max_length= 20,
        required= True,
        widget = forms.TextInput(attrs = {'class' : 'input', 'placeholder' : 'Phone Number'})
    )

    email = forms.EmailField(
        label = "Email",
        max_length= 100,
        required= True,
        widget = forms.TextInput(attrs = {'class' : 'input', 'placeholder' : 'Email'})
    )

    case_name = forms.CharField(
        label = "Case Name",
        max_length = 30,
        required= True,
        widget = forms.TextInput(attrs = {'class' : 'input', 'placeholder' : 'Case Name'})
    )

    victim_name = forms.CharField(
        label = "Victim Name/Alias",
        max_length = 60,
        required= False,
        widget = forms.TextInput(attrs = {'class' : 'input', 'placeholder' : 'Victim Name/Alias'})
    )

    victim_description = forms.CharField(
        label = "Victim Description",
        required= True,
        widget = forms.Textarea(attrs = {'class' : 'description', 'placeholder' : 'Victim Description', 'rows' : 10, 'cols' : 50})
    )

    crime_place = forms.CharField(
        label = "Crime Place",
        max_length = 150,
        required= True,
        widget = forms.TextInput(attrs = {'class' : 'input', 'placeholder' : 'Crime Place Description'})
    )

    chronology  = forms.CharField(
        label = "Chronology",
        required= True,
        widget = forms.Textarea(attrs = {'class' : 'description', 'placeholder' : 'Chronology', 'rows' : 10, 'cols' : 50})
    )