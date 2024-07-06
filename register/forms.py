from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    birth_date = forms.DateField(required=True, widget=forms.SelectDateWidget(years=range(1900, 2024)))
    height = forms.FloatField(required=True)
    weight = forms.FloatField(required=True)
    dropdown_field = forms.ChoiceField(choices=[
        ('gluten-free', 'Gluten-Free'),
        ('diabetes-friendly', 'Diabetes'),
        ('low-sodium', 'Low-Sodium'),
        ('autism-friendly', 'Autism')
        ])

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'birth_date', 'height', 'weight', 'dropdown_field']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email is already in use.")
        return email
    
class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'autofocus': True}))