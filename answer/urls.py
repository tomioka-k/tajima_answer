from django.conf.urls import include
from django.urls import path
from .views import IndexView, QuestionCreateView, QuestionDetailView, QuestionEditView

app_name = 'answer'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', QuestionCreateView.as_view(), name='create'),
    path('<int:pk>/', QuestionDetailView, name='detail'),
    path('<int:pk>/edit/', QuestionEditView.as_view(), name='edit'),
]
