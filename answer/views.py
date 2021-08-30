from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Classiffication, Question


class IndexView(generic.ListView):
    model = Question
    template_name = 'answer/index.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        classiffication = Classiffication.objects.all()
        context['classiffication'] = classiffication
        return context

# @login_required
# def index(request):
#     return render(request, 'index.html')
