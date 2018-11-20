from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices
from listings.models import Listing
from realtors.models import Realter

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    
    ctx = {
        'listings' : listings,
        'state_choices' : state_choices,
        'price_choices' : price_choices,
        'bedroom_choices' : bedroom_choices,
    }
    
    return render(request, 'pages/index.html', ctx)


def about(request):
    # Get all realtors

    realters = Realter.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realter.objects.all().filter(is_mvp=True)

    ctx = {
        'realtors' : realters, 'mvp_realtors' : mvp_realtors
    }

    return render(request, 'pages/about.html', ctx)
