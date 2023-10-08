from django.urls import path

from store import views


urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('product/<str:product_id>', views.product, name="product"),
]
