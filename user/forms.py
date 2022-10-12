from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserSignUp(UserCreationForm):
    class Meta:
        model = User
        fields = ["name", "surname", "username",
                  "email", "user_profile", "phone"]


class TutorSignUp(UserCreationForm):
    study_field = forms.CharField(required=True)
    experience = forms.CharField(required=True)
    teacher_number = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ["name", "surname", "username", "email", "user_profile"]
        


class LoginForm(forms.Form):
    email = forms.CharField(label="Email")
    password = forms.CharField(label="Parol", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})


class UserProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "surname", "username",
                  "email", "user_profile", "phone"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }
