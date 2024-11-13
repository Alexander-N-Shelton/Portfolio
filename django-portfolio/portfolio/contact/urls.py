#----- contact/urls.py -----#
from django.urls import path
from contact import views


urlpatterns = [
    path('', views.contact_view, name='contact'),
    path('contact/', views.success_view, name='success'),
]