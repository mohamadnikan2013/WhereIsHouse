from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Member(models.Model):
    primary_user = models.OneToOneField(User, related_name='member')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/',
                                        default='profile_pictures/funny-profile-pictures.jpg/')
    is_verified = models.BooleanField(default=False)
    email = models.EmailField(max_length=100, unique=True)
