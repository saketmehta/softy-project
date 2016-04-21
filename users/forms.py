from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    mobile_number = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")
        user = super(UserCreateForm, self).save(commit=True)
        user_profile = Profile(user=user, mobile_number=self.cleaned_data['mobile_number'])
        user_profile.save()
        return user, user_profile