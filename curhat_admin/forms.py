from django import forms

class replyCurhatForm(forms.Form):

    title = forms.CharField(
        label = "Title",
        max_length= 100,
        required= True,
        widget = forms.TextInput(attrs = {'class' : 'form-control', 'id' : 'title'})
    )

    description = forms.CharField(
        label = "Your Reply",
        max_length= 500,
        required= True,
        widget = forms.Textarea(attrs = {'class' : 'form-control','rows' : 5, 'id' : 'description'})
    )