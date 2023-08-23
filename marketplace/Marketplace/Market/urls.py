from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about),
    path('create/', views.create_product, name='create_product'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('delete_product_from_cart/<int:product_id>/', views.delete_product_from_cart, name='delete_from_cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path(' edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('filter/', views.filter_products_by_price, name='your_search_url_name')

]
handler404 = 'Market.views.custom_404_view'
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
