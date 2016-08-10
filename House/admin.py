from django.contrib import admin

# Register your models here.
from House.models import Home, Comment

admin.site.register(Home)
admin.site.register(Comment)