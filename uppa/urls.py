from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('departments/', views.departments, name='departments'),
    path('contact/', views.contact, name='contact'),
    path('team/', views.team, name='team'),
    path('projects/', views.projects, name='projects'),
    path('health/', views.health, name='health'),
]
