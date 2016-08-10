from django.conf.urls import url

from account.views import JoinView, Login, Edit_profile


urlpatterns = [
    url(r'^join/$', JoinView.as_view(), name='join'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', 'account.views.logout', name='logout'),
    url(r'^update/$', Edit_profile.as_view(), name='update'),
]
