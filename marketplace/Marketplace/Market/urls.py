from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about),
    path('create/', views.create_product, name='create_product'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)