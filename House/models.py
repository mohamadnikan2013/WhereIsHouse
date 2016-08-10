from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from account.models import Member

# Create your models here.

from account.models import Member


class Home(models.Model):
    member = models.ForeignKey(Member, null=True, related_name='houses')
    site = models.CharField(max_length=10, null=True)
    response_time = models.CharField(max_length=25, null=True)
    phone = models.CharField(null=True, max_length=20, validators=[RegexValidator(regex=r'0(.*)')])
    email = models.CharField(null=True, max_length=50)
    token = models.CharField(blank=False, max_length=50, unique=True)
    title = models.CharField(max_length=100)
    price1 = models.IntegerField(blank=True, null=True)
    price2 = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(max_length=50, auto_now=True)
    image_url = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True)
    square = models.IntegerField(null=True)
    room_num = models.IntegerField(null=True)
    region = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='House_picture/',
                              default='House_picture/House.jpeg/')
    like = models.IntegerField(default=0)
    member_like = models.ManyToManyField(Member, null=True)

    def clean(self):
        if self.price1 <= 0:
            raise ValidationError({'price1': 'price should be positive'})
        if self.price2 <= 0:
            raise ValidationError({'price2': 'price should be positive'})
        if self.square <= 0:
            raise ValidationError({'square': "square should be positive"})


class Comment(models.Model):
    member = models.ForeignKey(Member, related_name='comment')
    house = models.ForeignKey(Home, related_name='comment')
    text = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    replies = models.ManyToManyField('self', related_name='root_reply', null=True, blank=True)
    is_reply = models.BooleanField(default=False)

    def as_dict(self):
        return {
            'text': self.text,
            'date': self.date,
            'author_name': self.member.first_name + ' ' + self.member.last_name,
            'author_picture': self.member.profile_picture.url,
            'replies': [comment.as_dic_2() for comment in self.replies.all()],
            'comment_pk': self.pk,

        }

    def as_dic_2(self):
        return {
            'text': self.text,
            'date': self.date,
            'author_picture': self.member.profile_picture.url,
            'author_name': self.member.first_name + ' ' + self.member.last_name,
        }
