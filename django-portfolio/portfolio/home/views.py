#----- portfolio/home/views.py -----#
from django.shortcuts import render


def home_page(request):
    return render(request, 'home/main.html')