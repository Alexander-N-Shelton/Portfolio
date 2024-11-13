#----- skills/urls.py -----#

from django.urls import path
from skills import views

urlpatterns = [
    path('', views.skills_page, name='skills'),
]