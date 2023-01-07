from django.urls import path
from auth_app import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),
    path('', views.signin),
    path('logout-view/', views.logout_view, name='logout')

]
