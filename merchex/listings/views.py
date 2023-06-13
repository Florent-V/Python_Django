from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
from listings.models import Listing

def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django !</h1>
        <p>Mes groupes préférés sont :<p>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
        </ul>
""")

def about(request):
    return HttpResponse('<h1>A propos</h1> <p>Site de vente de produits dérivés</p>')

def contact(request):
    return HttpResponse('<h1>Contact</h1> <p>Contactez-nous</p>')

def listing(request):
    listings = Listing.objects.all()
    # return render(request, 'listing.html', {'name': 'Listing'})
    return HttpResponse(f"""
        <h1>Hello Django !</h1>
        <p>Les éléments de ma liste sont :</p>
        <ul>
            {"".join([f"<li>{listing.title}</li>" for listing in listings])}
        </ul>
    """)
