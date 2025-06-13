from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'What\'s happening?'}),
            'photo': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }
        labels = {
            'text': 'enter your tweet',
            'photo': 'Add a photo (optional)',
        }
        help_texts = {
            'text': 'You have 280 characters left.',
        }

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email', max_length=254)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')