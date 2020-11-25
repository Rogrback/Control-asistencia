from django import forms

class NewTeacherForm(forms.Form):
    id_card = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=9)
    user = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    user_type = forms.CharField(max_length=50)

