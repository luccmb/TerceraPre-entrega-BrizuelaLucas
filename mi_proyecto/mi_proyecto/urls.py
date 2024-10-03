from django.contrib import admin
from django.urls import path
from mi_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('add-product/', views.add_product, name='add_product'),
    path('search-product/', views.search_product, name='search_product'),
]
