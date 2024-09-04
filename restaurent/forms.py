from django import forms

class ReserveForm(forms.Form):
    reserved_table = forms.CharField(widget=forms.HiddenInput())