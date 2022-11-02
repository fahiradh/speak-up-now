from django import forms

class laporanResponseForm(forms.Form):
    status_case = forms.ChoiceField(
        # id="status",
        label = "Status Pelaporan",
        required= True,
        choices= [
        (None, '-Select Status-'),
        (True , 'On Process'),
        (False , 'Rejected'),
        ],
        widget = forms.Select(attrs = {'class' : 'select', 'class' : 'form-control'})
    )

    message = forms.CharField(
        # id="message",
        label = "Add Short Message",
        max_length= 50,
        required= True,
        widget = forms.Textarea(attrs = {'class' : 'form-control'})
    )