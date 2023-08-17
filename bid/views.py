from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "bid/base.html")

def auctions(request):
    return HttpResponse("Hello, world. You're at the bid auctions.")
