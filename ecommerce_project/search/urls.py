from django.urls import path
from . import views

app_name='search'

urlpatterns = [
    path('', views.ProductSearch.as_view(), name='allprodcat'),
    path('product/', views.ProductSearch.as_view(), name='product_search'),

]
