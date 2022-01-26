from django import forms
class HomePageForm(forms.Form):
    email      = forms.CharField (widget=forms.TextInput(attrs={'placeholder':'Email'}))
    message    = forms.CharField (widget=forms.Textarea(attrs={'placeholder':'message'}))