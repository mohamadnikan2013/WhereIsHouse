# Create your views here.
import json
import time

import requests
from django.core import serializers
from django.core.urlresolvers import reverse_lazy, reverse
from django.forms import modelform_factory
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import View
from django.views.generic.edit import FormView, UpdateView, DeleteView, FormMixin
import string, random

from House.Forms.form import NewAdvertiseForm, CommentForm
from House.models import *


def first(request):
    # print(request.user)
    return render(request, "firstpage.html")


def more(request, city, query_id):
    query_id = int(query_id)
    queryset = Home.objects.all()
    show_num = 20
    if city != "total":
        queryset = queryset.filter(region=city)
    else:
        queryset = queryset[show_num * query_id:show_num * (query_id + 1)]
    my_json = serializers.serialize('json', queryset)
    # print(my_json)
    return HttpResponse(my_json, content_type='application/json')


# def search(request, city, Id):
#     Id = int(Id)
#     show_num = 20
#     my_query = Home.objects.all().filter(region=city)[show_num * Id:show_num * (Id + 1)]
#     my_json = serializers.serialize('json', my_query)
#     return HttpResponse(my_json, content_type='application/json')
#
#
# def sheypoor(request):
#     site_responsetime = 0
#     counter = 0
#     while True:
#         payload = {'take': 100, 'skip': 100 * counter, "requestDateTime": site_responsetime, "categoryId": 43603}
#         req = requests.get("http://www.sheypoor.com/api/v2/offer/optimizedlist", params=payload)
#         decoded_data = json.loads(req.text)
#         site_responsetime = decoded_data["requestDateTime"]
#         for i in decoded_data['items']:
#             obj = Home()
#             obj.token = i['id']
#             if Home.objects.filter(token=obj.token).exists():
#                 return HttpResponse("finished")
#             else:
#                 url = "http://www.sheypoor.com/api/offer/optimized/%s" % i['id']
#                 try:
#                     req = requests.get(url)
#                     decoded_data = json.loads(req.text)
#                 except:
#                     pass
#                 obj.response_time = int(time.time())
#                 obj.name = decoded_data['ad']['name']
#                 obj.image = decoded_data['ad']['images'][0]['UrlGallery']
#                 obj.price1 = decoded_data['ad']['price']
#                 obj.description = decoded_data['ad']['description']
#                 obj.mobile = decoded_data['ad']['mobile']
#                 obj.site = 'sheypoor'
#                 try:
#                     obj.room_num = decoded_data['ad']["attributes"][2]['Value']
#                 except:
#                     pass
#                 obj.time = decoded_data['ad']['date']
#                 obj.region = decoded_data['ad']['region']['name']
#                 obj.city = decoded_data['ad']['city']['name']
#                 obj.save()
#             counter += 1
#
#
# def divar(request):
#     city_list = {1: 'tehran', 2: 'karaj', 3: 'mashhad', 4: 'isfahan', 5: 'tabriz', 6: 'shiraz',
#                  7: 'ahvaz', 8: 'qom', 9: 'kermanshah', 10: 'orumie', 11: 'zahedan', 12: 'rasht',
#                  13: 'kerman', 14: 'hamedan', 15: 'arak', 16: 'yazd', 17: 'ardabil', 18: 'bandarabas',
#                  19: 'qazvib', 20: 'zanjan', 21: 'ghorghan', 22: 'sari', 23: 'dezfol', 24: 'abadan', 25: 'bushehr',
#                  26: 'brujerd', 27: 'khoramabad', 28: 'sanndaj', 29: 'islamshahr', 30: 'kashan', 31: 'najafabad',
#                  32: 'ilam', 33: 'kish', 34: 'birjand', 35: 'semnan', 36: 'shahrkord', 37: 'mahshahr', 38: 'yasooj'}
#     for j in city_list.keys():
#         unique = True
#         while unique:
#             last_time = 0
#             url = "http://r.divar.ir/json/"
#             payload = '{"jsonrpc":"2.0","method":"getPostList","id":1,' \
#                       '"params":[[["place2",0,["%s"]],["cat1",0,[143]]],%s]}' % (j, last_time)
#             try:
#                 req = requests.post(url, data=payload)
#                 decoded_data = json.loads(req.text)
#             except:
#                 continue
#             last_time = decoded_data['result']['last_post_date']
#             for i in decoded_data['result']["post_list"]:
#                 x = Home()
#                 token = i['token']
#
#                 payload = '{"jsonrpc":"2.0","method":"getPost","id":1,"params":["%s","W"]}' % token
#                 try:
#                     new_req = requests.post(url, data=payload)
#                     new_decode_data = json.loads(new_req.text)
#                 except ConnectionError:
#                     continue
#                 x.description = new_decode_data['result']['desc']
#                 x.time = new_decode_data['result']['lm']
#                 x.token = new_decode_data['result']['token']
#                 x.title = new_decode_data['result']['title']
#                 x.image = "http://www.sheypoor.com/image/5cb2d2/200x135_fp/img/placeholders/real-estate.jpg"
#                 x.response_time = int(time.time())
#                 x.region = city_list[j]
#                 x.city = city_list[j]
#                 x.phone = new_decode_data['result'].get('phone')
#                 x.site = "divar"
#                 x.email = new_decode_data['result'].get('email')
#                 x.square = new_decode_data['result'].get('v01')
#                 x.price1 = new_decode_data['result'].get('v09')
#                 x.price2 = new_decode_data['result'].get('v10')
#                 if Home.objects.all().filter(token=token).exists():
#                     unique = False
#                     break
#                 else:
#                     x.save()
#     return HttpResponse('finished saving all cities all new :D ;D ;D')


#
# def details(request, token):
#     house = Home.objects.get(token=token)
#     return render(request=request, template_name="details.html", context={'house': house})


class NewAdvertise(FormView):
    form_class = NewAdvertiseForm
    template_name = 'new.html'
    success_url = '/'

    # def post(self, request, *args, **kwargs):
    #     form = NewAdvertiseForm(self.request.POST, user=self.request.user)
    #     return super(NewAdvertise, self).post(request, *args, **kwargs)
    #

    def form_valid(self, form):
        inst = form.save(commit=False)
        inst.token += ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        inst.member = self.request.user.member
        inst.save()
        return super(NewAdvertise, self).form_valid(form)


class MyPosts(ListView):
    model = Home
    template_name = "myposts.html"

    def get_queryset(self):
        user = self.request.user
        query_set = Home.objects.all().filter(member=user.member)
        return query_set


class Edit(UpdateView):
    model = Home
    fields = ('phone', 'email', "title", 'price1', 'price2', 'square', 'room_num', 'region', 'city', 'image',)
    template_name = "edit.html"
    success_url = reverse_lazy('house:my-post')

    def get_object(self, queryset=None):
        Object = Home.objects.all().get(token=self.kwargs['token'])
        return Object


class Delete(DeleteView):
    model = Home
    success_url = reverse_lazy('house:my-post')
    template_name = 'delete.html'

    def get_object(self, queryset=None):
        Object = Home.objects.all().get(token=self.kwargs['token'])
        return Object

        # class Details(FormMixin, DetailView):
        #     model = Home
        #     form_class = CommentForm
        #     template_name = 'details.html'
        #
        #     # success_url = reverse_lazy('details')
        #
        #     def get_success_url(self):
        #         return reverse('house:Details', kwargs={'token': self.object.token})
        #
        #     def get_context_data(self, **kwargs):
        #         context = super(Details, self).get_context_data(**kwargs)
        #         context['form'] = self.get_form()
        #         return context
        #
        # def get_object(self, queryset=None):
        #     object = Home.objects.all().get(token=self.kwargs['token'])
        #     return object
        #
        # def post(self, request, *args, **kwargs):
        #     self.object = self.get_object()
        #     form = self.get_form()
        #     if form.is_valid():
        #         return self.form_valid(form)
        #     else:
        #         return self.form_invalid(form)
        #
        # def form_valid(self, form):
        #     instance = form.save(commit=False)
        #     instance.member = self.request.user.member
        #     instance.house = self.get_object()
        #     instance.save()
        #     return super(Details, self).form_valid(form)


class Details(DetailView):
    model = Home
    template_name = 'details.html'

    def get_object(self, queryset=None):
        object = Home.objects.all().get(token=self.kwargs['token'])
        return object


class Ajax(View):
    def get(self, request, *args, **kwargs):
        token = self.kwargs['token']
        comments = [comment.as_dict() for comment in Home.objects.get(token=token).comment.filter(is_reply=0).all()]
        return JsonResponse({'comments': comments})

    def post(self, request, *args, **kwargs):
        comment = Comment()
        comment.member = request.user.member
        comment.house = Home.objects.all().get(token=self.kwargs['token'])
        comment.text = request.POST['text']
        comment.save()
        return HttpResponse("ok the form is saved")


class Reply(View):
    form_class = Comment
    initial = {'key': 'value'}
    template_name = 'details.html'

    def get(self, request, *args, **kwargs):
        house_pk = self.kwargs['house_pk']
        home = Home.objects.all().get(pk=house_pk)
        member = request.user.member
        if member not in home.member_like.all():
            home.member_like.add(member)
            home.like += 1
            home.save()
            return HttpResponse('ok')
        else:
            return HttpResponse("liked before")

    def post(self, request, *args, **kwargs):
        comment_pk = self.kwargs['comment_pk']
        house_pk = self.kwargs['house_pk']
        home = Home.objects.all().get(pk=house_pk)
        comment = Comment.objects.all().get(pk=comment_pk)
        new_comment = Comment()
        new_comment.text = request.POST.get('text')
        new_comment.member = request.user.member
        new_comment.house = home
        new_comment.is_reply = True
        new_comment.save()
        comment.replies.add(new_comment)
        comment.save()
        return HttpResponse("form saved thank you")


class Suggest(View):
    def get(self, request, *args, **kwargs):
        suggest = self.kwargs["suggest"]
        my_suggest = Comment.objects.filter(text__contains=suggest).values('text')
        return JsonResponse({'my_suggest': list(my_suggest)})
