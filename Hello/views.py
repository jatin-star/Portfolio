from django.shortcuts import render
from django.http import HttpResponse


def Hello(request):
    return HttpResponse("Hello world!")

def portfolio_page(request):
    return render(request, "index.html")
