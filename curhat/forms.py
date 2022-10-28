from django import forms

years = [x for x in range(2022, 2025)]

class curhatForm(forms.Form):
    date = forms.DateField(
        label = "Date",
        widget = forms.SelectDateWidget(years = years, attrs = {'class' : 'select'})
    )

    name = forms.CharField(
        label = "Name/Initial",
        max_length= 100,
        required= True,
        widget = forms.TextInput(attrs = {'class' : 'input', 'placeholder' : 'Name', 'class' : 'form-control'})
    )

    title = forms.CharField(
        label = "Title",
        max_length= 100,
        required= True,
        widget = forms.TextInput(attrs = {'class' : 'input', 'placeholder' : 'Title', 'class' : 'form-control'})
    )

    description = forms.CharField(
        label = "Description",
        required= True,
        widget = forms.Textarea(attrs = {'class' : 'description', 'placeholder' : 'Description', 'rows' : 10, 'cols' : 50, 'class' : 'form-control'})
    )

    contactable = forms.ChoiceField(
        label = "Do you need consultation in interactive mode?",
        choices = [
            ("Y", "YES"),
            ("N", "NO"),
        ],
        widget = forms.Select(attrs = {'class' : 'select', 'class' : 'form-control'}),
    )
