from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.offdayapp, name='offdayapp'),  # Make sure the view name and URL pattern match
]
