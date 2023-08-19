from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import k_washing

# Create your views here.
class k_washingList(ListView):
    model = k_washing
    ordering = '-pk'

    
class k_washingCreate(LoginRequiredMixin, CreateView):
    model = k_washing
    fields = ['floor','direction', 'time', 'content']

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            response = super(k_washingCreate, self).form_valid(form)

            return response
        else:
            return redirect('/k_washing/')