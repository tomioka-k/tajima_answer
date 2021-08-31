from django.core.checks import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Classiffication, Question, Reply
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
    form_class = QuestionForm

    def get_success_url(self):
        return reverse('answer:detail', kwargs={'pk': self.object.pk})


@require_POST
def delete_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.user == question.user:
        question.delete()
        return redirect('answer:index')
    return redirect('answer:detail', pk=pk)


@require_POST
def delete_reply(request, question_id, pk):
    reply = get_object_or_404(Reply, pk=pk)
    if request.user == reply.user:
        reply.delete()
    return redirect('answer:detail', pk=question_id)


def ReplyEditView(request, question_id, pk):
    template_name = 'answer/reply_edit.html'
    question = get_object_or_404(Question, pk=question_id)
    reply = get_object_or_404(Reply, pk=pk)
    form = ReplyForm(instance=reply)
    if request.method == 'GET':
        return render(request, template_name, {'object': question, 'reply_id': pk, 'form': form})

    if request.method == 'POST':
        post_form = ReplyForm(request.POST, instance=reply)
        if post_form.is_valid():
            post_form.save()
    return redirect('answer:detail', pk=question_id)
