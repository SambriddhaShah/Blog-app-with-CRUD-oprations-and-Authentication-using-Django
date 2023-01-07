from django.urls import path
from content_app import views

urlpatterns = [
path('home/', views.home, name='home'),
path('add/', views.add, name='add'),
path('delete/<int:id>', views.delete, name='delete'),
path('edit/<int:id>', views.edit, name='edit'),
path('deleteall', views.deleteall, name='deleteall')

]
