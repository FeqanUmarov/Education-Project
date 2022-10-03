from .models import UserQuery, TutorQuery
from django.forms import ModelForm
from django import forms

class QueryForm(forms.ModelForm):
    class Meta:
        model = UserQuery
        fields = '__all__'

class TutorQueryForm(forms.ModelForm):
    class Meta:
        model = TutorQuery
        fields = '__all__'