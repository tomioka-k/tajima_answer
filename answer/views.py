from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic.base import View
from .models import Classiffication, Question
from .forms import QuestionForm, ReplyForm


class IndexView(LoginRequiredMixin, generic.ListView):
    model = Question
    template_name = 'answer/index.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        classiffication = Classiffication.objects.all()
        context['classiffication'] = classiffication
        return context


class QuestionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Question
    template_name = 'answer/create.html'
    form_class = QuestionForm

    def form_valid(self, form):
        question = form.save(commit=False)
        question.user = self.request.user
        question.save()
        return redirect('answer:index')


@login_required
def QuestionDetailView(request, pk):
    template_name = 'answer/detail.html'
    object = get_object_or_404(Question, pk=pk)
    form = ReplyForm
    if request.method == 'GET':
        return render(request, template_name, {'object': object, 'form': form})

    if request.method == 'POST':
        post_form = ReplyForm(request.POST)
        if post_form.is_valid():
            reply = post_form.save(commit=False)
            reply.question = object
            reply.user = request.user
            reply.save()
        return render(request, template_name, {'object': object, 'form': form})


class QuestionEditView(LoginRequiredMixin, generic.UpdateView):
    model = Question
    template_name = 'answer/edit.html'
    fields = ['content', ]

    def get_success_url(self):
        return reverse('answer:detail', kwargs={'pk': self.object.pk})
