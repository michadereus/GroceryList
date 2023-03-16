from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Item

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('items')

class RegisterView(FormView):
    template_name = "base/register.html"
    form_class = UserCreationForm
    # redirect_authenticated_user = True
    success_url = reverse_lazy('items')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('items')
        return super(RegisterView, self).get(*args, **kwargs)

class ItemList(LoginRequiredMixin, ListView):
    model = Item
    context_object_name = 'items'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = context['items'].filter(user=self.request.user)
        context['count'] = context['items'].filter(in_basket=False).count()
        context['in_basket'] = context['items']
        # search_input = self.request.GET.get()'search-area'
        return context

class ItemDetail(LoginRequiredMixin, DetailView):
    model = Item
    context_object_name = 'item'
    template_name = 'base/item.html' 


class ItemCreate(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['item_name', 'quantity', 'in_basket']
    success_url = reverse_lazy('items')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ItemCreate, self).form_valid(form)

class ItemUpdate(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ['item_name', 'quantity', 'in_basket']
    success_url = reverse_lazy('items')


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    context_object_name = 'item'
    success_url = reverse_lazy('items')
    
# class ItemInBasket(LoginRequiredMixin, View):
#     model = Item
#     context_object_name = 'item'
#     success_url = reverse_lazy('items')

