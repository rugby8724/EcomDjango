from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group, User

from . import forms
# Create your views here.
class Signup(CreateView):
    form_class = forms.CustomerCreateForm
    success_url = reverse_lazy('store:home')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        view = super(Signup, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        group = Group.objects.get(name='Customer')
        user.groups.add(group)
        login(self.request, user)
        return view
