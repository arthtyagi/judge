from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, RedirectView
from django.db.models import Q
from . import compare

from .models import Question, Answer


class CoderListView(ListView):
    model = Question
    template_name = "coder/coder_list.html"
    context_object_name = 'question'


class CoderDetailView(DetailView):
    model = Question
    template_name = "coder/coder_detail.html"
    context_object_name = 'question'


class CoderCreateView(CreateView):
    model = Answer
    fields = ['result']
    context_object_name = 'answer'
    template_name = "coder/coder_form.html"

    def get_success_url(self):
        question = self.object.question
        return reverse('coder:detail', kwargs={'pk': question.id})

    def form_valid(self, form):
        question = Question.objects.get(id=self.kwargs['qid'])
        form.instance.question = question
        form.instance.is_correct = compare.compare( solution=
            self.request.FILES[(question.solution)], result = self.request.FILES[(form.instance.result)])
        return super().form_valid(form)


"""
	def upload_file(request):
		if request.method == 'POST':
			form = UploadFileForm(request.POST, request.FILES)
			if form.is_valid():
				compare.compare(request.FILES['file'])
				return HttpResponseRedirect('/success/url/')
		else:
			form = UploadFileForm()
		return render(request, 'upload.html', {'form': form})
"""
