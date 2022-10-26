from django import forms
from curhat import models

class curhatForm(forms.Form):
    name = forms.CharField(
        label = "Name/Initial",
        max_length= 100,
        required= True,
        widget = forms.TextInput(attrs = {'class' : 'input', 'placeholder' : 'Name'})
    )

    title = forms.CharField(
        label = "Title",
        max_length= 100,
        required= True,
        widget = forms.TextInput(attrs = {'class' : 'input', 'placeholder' : 'Title'})
    )

    description = forms.CharField(
        label = "Description",
        required= True,
        widget = forms.Textarea(attrs = {'class' : 'description', 'placeholder' : 'Description', 'rows' : 10, 'cols' : 50})
    )

    contactable = forms.ChoiceField(
        label = "Need consultation in interactive mode?",
        choices = [
            ("Y", "YES"),
            ("N", "NO"),
        ],
        widget = forms.Select(attrs = {'class' : 'select'}),
    )