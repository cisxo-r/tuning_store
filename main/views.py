from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_page(request):
    return render(request,'main/index.html')


def about(request):
    return render(request,'main/about.html')


def items(request):
    return render(request,'main/items.html')


def favorite(request):
    return render(request,'main/favorite.html')


def personal_office(request):
    return render(request,'main/office.html')
