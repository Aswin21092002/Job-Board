from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Employer, JobSeeker

class EmployerRegistrationForm(UserCreationForm):
    company_name = forms.CharField(max_length=255)
    website = forms.URLField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'company_name', 'website']

class JobSeekerRegistrationForm(UserCreationForm):
    resume = forms.FileField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'resume']
