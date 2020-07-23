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

    def get_queryset(self, *args, **kwargs):
        object_list = super(CoderListView, self).get_queryset(*args, **kwargs)
        search = self.request.GET.get('q', None)
        if search:
            object_list = object_list.filter(
                Q(title__contains=search) |
                Q(content__contains=search)
            )
            return object_list
        else:
            return object_list


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
 #   form.instance.question.iscorrect = compare.compare((
  #      list(self.request.FILES.values())[0], question.solution), (list(self.request.FILES.values())[0], form.instance.result))
  #  form.instance.iscorrect = compare.compare(
   #     (list(self.request.FILES.values())[
        #     0].file.read(), question.solution),
        #   (list(self.request.FILES.values())[
        #   0].file.read(), form.instance.result)
        # )
        f = (list(self.request.FILES.values())[0],
             str(question.solution.read()))

        f1 = (list(self.request.FILES.values())[0],
              str(form.instance.result.read()))

        form.instance.iscorrect = compare.compare(f, f1)
        if form.instance.iscorrect:
            form.instance.question.iscorrect = True

        form.save()
        form.instance.question.save()
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
