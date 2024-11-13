#----- urls.py -----#
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls'), name='home'),
    path('admin/', admin.site.urls),
    path('about/', include('about.urls'), name='about'),
    path('resume/', include('resume.urls'), name='resume'),
    path('contact/', include('contact.urls'), name='contact'),
    path('skills/', include('skills.urls'), name='skills'),
    path('projects/', include('projects.urls'), name='projects'),
]
