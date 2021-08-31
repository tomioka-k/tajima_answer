from django.conf.urls import include
from django.urls import path
from .views import IndexView, QuestionCreateView, QuestionDetailView, QuestionEditView, delete_question, delete_reply, ReplyEditView

app_name = 'answer'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', QuestionCreateView.as_view(), name='create'),
    path('<int:pk>/', QuestionDetailView, name='detail'),
    path('<int:pk>/edit/', QuestionEditView.as_view(), name='edit'),
    path('<int:pk>/delete/', delete_question, name='delete'),
    path('<int:question_id>/reply/<int:pk>/delete',
         delete_reply, name='delete-reply'),
    path('<int:question_id>/reply/<int:pk>/edit/',
         ReplyEditView, name='edit-reply'),
]
