from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('register/', views.register_view, name='register'),
    # path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
    path('locations_add/', views.locations_add, name='locations_add'),
]
