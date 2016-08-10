from django.contrib.auth.models import User
from django.forms import ModelForm, fields_for_model, forms

from House.models import Home, Comment


class NewAdvertiseForm(ModelForm):
    class Meta:
        model = Home
        fields = ("phone", "email", 'title', 'price1', 'price2', 'square', 'image', 'city', 'description')


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)
