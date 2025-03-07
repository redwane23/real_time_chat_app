from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from home.models import Profile
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username",'password1','password2']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'username', 'bio']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }
    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        # Make all fields non-required (or specify individually)
        self.fields['profile_picture'].required = False
        self.fields['username'].required = False
        self.fields['bio'].required = False