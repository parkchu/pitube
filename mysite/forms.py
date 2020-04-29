from account.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    profile = forms.ImageField(required=True)

    class Meta:
        model = User
        fields = ("user", "email", "profile", "password1", "password2")

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.profile = self.cleaned_data["profile"]
        if commit:
            user.save()
        return user