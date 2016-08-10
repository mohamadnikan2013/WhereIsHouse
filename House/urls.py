from django.conf.urls import url

from House.views import Details, NewAdvertise, MyPosts, Edit, Delete, Reply, Ajax , Suggest

urlpatterns = [
    # url(r'^index/sheypoor/', 'House.views.sheypoor'),
    # url(r'^index/divar/', 'House.views.divar'),
    url(r'^more/(\w+)/(\d+)', 'House.views.more'),
    # url(r'^search/(\w+)/(\d+)', 'House.views.search'),
    url(r'^details/(?P<token>\w+)/$', Details.as_view(), name='details'),
    url(r'^new/$', NewAdvertise.as_view(), name='new-advertise'),
    url(r'^myposts/$', MyPosts.as_view(), name='my-post'),
    url(r'^edit/(?P<token>\w+)/$', Edit.as_view(), name='edit-my-post'),
    url(r'^delete/(?P<token>\w+)/$', Delete.as_view(), name='delete-my-post'),
    url(r'^reply/(?P<house_pk>\w+)/(?P<comment_pk>\w+)/$', Reply.as_view(), name='reply'),
    url(r'^ajax/(?P<token>\w+)/$', Ajax.as_view(), name='ajax'),
    url(r'^suggest/(?P<suggest>\w+)/$', Suggest.as_view(), name='suggest'),
]
