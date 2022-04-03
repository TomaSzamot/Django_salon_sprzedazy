from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_page, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('', views.home, name="home"),
    path('user/', views.user_Page, name="user-page"),
    path('products/', views.products, name="products"),
    path('create_client/', views.create_client, name="create_client"),
    path('client/<str:pk>/', views.client, name="client"),

    path('create_order/', views.create_order, name="create_order"),
    path('create_car/', views.create_car, name="create_car"),

    path('update_order/<str:pk>/', views.update_order, name="update_order"),
    path('delete_order/<str:pk>/', views.delete_order, name="delete_order"),
]