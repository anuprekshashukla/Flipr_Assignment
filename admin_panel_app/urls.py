from django.urls import path
from . import views

urlpatterns = [
   # path('', views.home, name='home'),  # Define a view for the root URL
    path('list_instances/', views.list_instances, name='list_instances'),
    # Add other URL patterns for database management, user management, etc.
]
