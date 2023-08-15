from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('Market.urls')),
    path('accounts/', include('Users.urls')),
    path('', views.index, name='lobby')
]
