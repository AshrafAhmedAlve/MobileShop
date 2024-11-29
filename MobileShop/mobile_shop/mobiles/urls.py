from django.urls import path
from . import views

urlpatterns = [
    path('', views.mobile_list, name='mobile_list'),
    path('add/', views.add_mobile, name='add_mobile'),
    path('edit/<int:id>/', views.edit_mobile, name='edit_mobile'),  
    path('delete/<int:id>/', views.delete_mobile, name='delete_mobile'),
]
