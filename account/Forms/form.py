import re

from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms.models import ModelForm, fields_for_model

from House.models import Member


class JoinForm(ModelForm):
    username = fields_for_model(User)['username']
    password = fields_for_model(User)['password']
    re_password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(JoinForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()
        self.fields['email'].widget = forms.EmailInput()
        self.fields['email'].required = True

    class Meta:
        model = Member
        fields = ('first_name', 'last_name', 'email', 'birth_date')

    def clean(self):
        cleaned_data = super(JoinForm, self).clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        if User.objects.all().filter(username=username).exists():
            raise forms.ValidationError('Username "%s" is already in use.' % username)
        if Member.objects.all().filter(email=email).exists():
            raise forms.ValidationError('Email "%s" is already in use.' % email)
        if cleaned_data.get('password') != cleaned_data.get('re_password'):
            raise ValidationError("the password doesnt match", code='invalid')

    def save(self, commit=True):
        instance = super(JoinForm, self).save(commit=False)
        data = self.cleaned_data
        user = User.objects.create_user(username=data.get('username'), password=data.get('password'))
        if commit:
            user.save()
            instance.primary_user = user
            instance.save()
        return instance


class LoginForm(forms.Form):
    username = forms.CharField(required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    def clean(self):
        data = self.cleaned_data
        user = authenticate(username=data.get('username'),
                            password=data.get('password'))
        if not user:
            raise forms.ValidationError(
                {'username': 'Invalid username or password'})
