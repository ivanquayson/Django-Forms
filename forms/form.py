from django import forms


class InputForm(forms.Form):

    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    roll_number = forms.IntegerField(help_text="Enter a six digit number roll")

    password = forms.CharField(widget=forms.PasswordInput())