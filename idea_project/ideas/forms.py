from django import forms
from .models import Idea, SignupDetail,Message,InvestorProfile

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['title', 'description', 'tag']

TAG_CHOICES = [
    ('Technology', 'Technology'),
    ('Health', 'Health'),
    ('Finance', 'Finance'),
    ('Education', 'Education'),
    ('Environment', 'Environment'),
    ('Marketing', 'Marketing'),
    ('Startups', 'Startups'),
    ('Sustainability', 'Sustainability'),
    ('AI', 'AI'),
    ('Blockchain', 'Blockchain'),
    ('E-commerce', 'E-commerce'),
    ('Social Media', 'Social Media'),
    ('Cybersecurity', 'Cybersecurity'),
    ('Robotics', 'Robotics'),
    ('Fintech', 'Fintech'),
    ('Legal Tech', 'Legal Tech'),
    ('Gaming', 'Gaming'),
    ('Augmented Reality', 'Augmented Reality'),
    ('Virtual Reality', 'Virtual Reality'),
    ('Travel', 'Travel'),
    ('Real Estate', 'Real Estate'),
    ('Food & Beverage', 'Food & Beverage'),
    ('Telecommunications', 'Telecommunications'),
]

class InvestorProfileForm(forms.ModelForm):
    class Meta:
        model = InvestorProfile
        fields = ['name', 'email', 'tags']
    
    tags = forms.ChoiceField(
        choices=TAG_CHOICES,
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        required=True,
    )

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class SignupForm(forms.ModelForm):
    class Meta:
        model = SignupDetail
        fields = ['name', 'email', 'password', 'category']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Type your message...'}),
        }

