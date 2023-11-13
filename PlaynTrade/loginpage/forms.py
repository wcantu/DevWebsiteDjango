from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import SiteUser  # Ensure this import points to your custom user model

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email Address', required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = SiteUser  # Reference to your custom user model
        fields = ('email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if SiteUser.objects.filter(email=email).exists():
            raise forms.ValidationError("An account with this email already exists.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']  # Use the email as the username
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
