from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, RedirectView
from django.db.models import Q
from .models import Question, Answer

from .forms import ResultForm

def home(request):
    return render(request, 'coder/coder_list.html', {'title': 'Home'})

class CoderListView(ListView):
    model = Question
    template_name = "coder/coder_list.html"

class CoderDetailView(DetailView):
    model = Question
    template_name = "coder/coder_detail.html"
    
class CoderCreateView(CreateView):
    model = Answer
    template_name = "coder/coder_form.html"
    
