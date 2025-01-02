from django import forms
from .models import student

# data insertion form
class datain(forms.ModelForm):
    class Meta:
        model = student
        fields = [ 'nic', 'name', 'resident' ]
        widgets = {
            'nic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter NIC number'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'resident': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Resident'}),
        }


# search items form
class search(forms.Form):
    nic = forms.CharField(max_length=20, required=False, label="NIC")
    name = forms.CharField(max_length=100, required=False, label="Name")
    resident = forms.CharField(max_length=100, required=False, label="Resident")


# update items form
class update(forms.ModelForm):
    class Meta:
        model = student
        fields = ['nic', 'name', 'resident']
        widgets = {
            'nic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter NIC number'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'resident': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Resident'}),
        }