from django import forms

STATUS_CHOICES= [
    ('On Process', True),
    ('Rejected', False),
    ]

class laporanResponseForm(forms.Form):
    status_case = forms.ChoiceField(
        id="status",
        label = "Status Pelaporan",
        required= True,
        widget = forms.RadioSelect(choices=STATUS_CHOICES)
    )

    message = forms.CharField(
        id="message",
        label = "Add Short Message",
        max_length= 50,
        required= True,
        widget = forms.Textarea(attrs = {'class' : 'form-control'})
    )