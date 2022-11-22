from django.urls import path
from django.contrib.auth import views as auth_views

from myapp import views as user_views

app_name = 'myapp'

urlpatterns = [
    path('', user_views.home, name='home'),
    path(r'register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='myapp/logout.html'), name='logout'),
    path(r'category/', user_views.category, name='category'),
    path(r'show_category/', user_views.show_category, name='show_category'),
    path(r'edit_product/<str:pk>', user_views.edit_product, name='edit_product'),
    path(r'delete_product/<str:pk>', user_views.delete_product, name='delete_product')

]
