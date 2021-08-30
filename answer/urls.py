from django.conf.urls import include
from django.urls import path
from .views import IndexView, CreateView

app_name = 'answer'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', CreateView.as_view(), name='create'),

]
