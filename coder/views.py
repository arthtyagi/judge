from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, RedirectView
from django.db.models import Q

from .forms import ResultForm

def home(request):
    return render(request, 'coder/coder.html', {'title': 'Home'})

