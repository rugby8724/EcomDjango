from django.urls import path
from . import views

app_name='store'

urlpatterns = [
    path('', views.HomePage.as_view(), name="home"),
    path('category/<slug:slug>/', views.SingleCategory.as_view(), name='category'),
    path('product/<slug:slug>/', views.SingleProduct.as_view(), name='product'),
    path('cart/add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('cart/delete/<int:product_id>/', views.cart_remove_product, name='remove_product'),
    path('cart/', views.cart_detail, name='cart'),
    path('thanks/<int:pk>/', views.SingleOrder.as_view(), name='thanks'),
    path('history/', views.OrderList.as_view(), name='order_history'),
    path('detail/<int:pk>/', views.OrderDetail.as_view(), name='order_detail')
]
