#----- projects/urls.py -----#
from django.urls import path
from projects import views

urlpatterns = [
    path('', views.projects_view, name='projects'),
]