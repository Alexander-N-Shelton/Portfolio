#----- projects/views.py -----#
from django.shortcuts import render

def projects_view(request):
    return render(request, 'projects/projects.html')