from django.urls import path
from . import views

urlpatterns = [
    # This maps the "empty" path of the app to a view
    path('', views.index, name='index'), 
]