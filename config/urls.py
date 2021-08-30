from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('answer/', include('answer.urls'), name='answer'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('auth/', include('social_django.urls', namespace='social')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
