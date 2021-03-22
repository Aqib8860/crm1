from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<str:cus_id>/', views.customer, name='customer'),
    path('create_order/<str:cus_id>', views.create_order, name='create_order'),
    path('update_order/<str:order_id>', views.update_order, name='update_order'),
    path('delete_order/<str:order_id>', views.delete_order, name='delete_order'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('user_page/', views.user_page, name='user_page'),
    path('user_settings', views.user_settings, name='user_settings'),

]
