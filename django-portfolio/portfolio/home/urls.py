#----- portfolio/home/urls.py -----#
from django.urls import path
from home import views


urlpatterns = [
    path('', views.home_page, name='home'),
]