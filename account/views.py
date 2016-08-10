from django.conf import settings
from django.contrib.auth import logout as django_logout, authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import FormView, UpdateView
from rest_framework.reverse import reverse_lazy

from account.Forms.form import JoinForm, LoginForm

# Create your views here.
from django.views.generic import CreateView

from account.models import Member


class JoinView(CreateView):
    model = User
    template_name = 'join.html'
    form_class = JoinForm

    def __init__(self):
        super(JoinView, self).__init__()
        self.member = None

    def form_valid(self, form):
        django_logout(self.request)
        self.member = form.save()
        # login(self.request, self.member)
        return redirect('FirstPage')


class Login(FormView):
    form_class = LoginForm
    template_name = "login.html"
    success_url = 'FirstPage'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        login(self.request, authenticate(username=username, password=password))
        return redirect(self.success_url)


def logout(request):
    django_logout(request)
    return redirect('FirstPage')


class Edit_profile(UpdateView):
    model = Member
    fields = ('first_name', 'last_name', "email", "profile_picture",)
    success_url = reverse_lazy('FirstPage')
    template_name = "update.html"

    def get_object(self, **kwargs):
        return self.request.user.member
