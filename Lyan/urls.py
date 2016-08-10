"""Lyan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static

import House.urls
import account.urls
from Lyan import settings


urlpatterns = [
                  url(r'^account/', include(account.urls, namespace='account')),
                  url(r'^house/', include(House.urls, namespace='house')),
                  url(r'^admin/', admin.site.urls),
                  url(r'^$', 'House.views.first', name='FirstPage'),
                  # url(r'^index/sheypoor/', 'House.views.sheypoor'),
                  # url(r'^index/divar/', 'House.views.divar'),
                  # url(r'^more/(\w+)/(\d+)', 'House.views.more'),
                  # url(r'^search/(\w+)/(\d+)', 'House.views.search'),
                  # url(r'^details/(?P<token>\w+)/$', Details.as_view(), name='details'),
                  # url(r'^Join/$', JoinView.as_view()),
                  # url(r'^login/$', Login.as_view()),
                  # url(r'^logout/$', 'account.views.logout'),
                  # url(r'^update/$', Edit_profile.as_view()),
                  # url(r'^new/$', NewAdvertise.as_view()),
                  # url(r'^myposts/$', MyPosts.as_view(), name='myposts'),
                  # url(r'^edit/(?P<token>\w+)/$', Edit.as_view(), name='myposts'),
                  # url(r'^delete/(?P<token>\w+)/$', Delete.as_view(), name='myposts'),
                  # url(r'^reply/(?P<house_pk>\w+)/(?P<comment_pk>\w+)/$', Reply.as_view(), name='reply'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
