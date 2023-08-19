from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

def index(request):
    auctions = Auction.objects.all()
    context = {'auctions': auctions}
    return render(request, "bid/auctions_list.html", context)

def create(request):
    form = AuctionForm()
    context = {'form': form}
    return render(request, "bid/auction_create.html",context)

def auctions(request,catId):
    auctions = Auction.objects.filter(category=catId)
    context = {'auctions': auctions}
    return render(request, "bid/auctions_list.html", context)
