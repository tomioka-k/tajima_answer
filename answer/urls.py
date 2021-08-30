from django.conf.urls import include
from django.urls import path
from .views import IndexView

app_name = 'answer'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),

]
