from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Classiffication, Question
from .forms import QuestionForm


class IndexView(LoginRequiredMixin, generic.ListView):
    model = Question
    template_name = 'answer/index.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        classiffication = Classiffication.objects.all()
        context['classiffication'] = classiffication
        return context


class CreateView(LoginRequiredMixin, generic.CreateView):
    model = Question
    template_name = 'answer/create.html'
    form_class = QuestionForm

    def form_valid(self, form):
        question = form.save(commit=False)
        question.user = self.request.user
        question.save()
        return redirect('answer:index')
