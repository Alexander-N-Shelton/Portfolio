#----- portfolio/about/urls.py -----#
from django.urls import path
from about import views


urlpatterns = [
    path('', views.about_page, name='about'),
]