#----- resume/urls.py -----#
from django.urls import path
from resume import views


urlpatterns = [
    path('', views.resume_page, name='resume'),
]
