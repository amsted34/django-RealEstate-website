from django.shortcuts import render
from .models import Listing


def index(request):
    # get all the listings object
    listings = Listing.objects.all()
    # variable of type dictionary that will hold the listings
    context = {
        'listings': listings
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
