from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email
from .models import User, Profile

class SignupForm(UserCreationForm):
    bio = forms.CharField(required=False)
    website_url = forms.URLField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.fields['username'].validators = [validate_email]
        self.fields['username'].help_text = 'Enter Email Format.'
        self.fields['username'].label = 'Email'

    def save(self):
        user = super().save(commit=True)
        user.email = user.username
        user.save() # user와 profile 이 서로 1:1관계이므로 user 객체가 생성되어야만 Profile 객체생성 가능

        bio = self.cleaned_data.get('bio', None)
        website_url = self.cleaned_data.get('website_url', None)

        Profile.objects.create(user=user, bio=bio, website_url=website_url)

        return user

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('bio', 'website_url')

    '''
    def clean_username(self):
        value = self.clean_data.get('username')
        if value:
            validate_email(value)
        return value
    '''

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'website_url']


























