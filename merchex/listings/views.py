from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
from listings.models import Listing
from listings.forms import BandForm, ContactUsForm, ListingForm
from django.core.mail import send_mail
from django.shortcuts import redirect  # ajoutez cet import


from django.forms.models import model_to_dict
import pprint

def band_list(request):
    bands = Band.objects.all()
    return render(request,
                  'listings/band_list.html',
                  {'bands': bands}
                  )

def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request,
                  'listings/band_detail.html',
                  {'band': band}
                  )

def band_create(request):
  if request.method == 'POST':
    form = BandForm(request.POST)
    if form.is_valid():
      band = form.save()
      return redirect('band_detail', band_id=band.id)
  else:
    form = BandForm()
  return render(request,
                'listings/band_create.html',
                {'form': form}
                )

def band_edit(request, band_id):
  band = Band.objects.get(id=band_id)
  if request.method == 'POST':
    form = BandForm(request.POST, instance=band)
    if form.is_valid():
      band = form.save()
      return redirect('band_detail', band_id=band.id)
  else:
    form = BandForm(instance=band)
  return render(request,
                'listings/band_edit.html',
                {'form': form}
                )

# def band_delete(request, band_id):
#   Band.objects.get(id=band_id).delete()
#   return redirect('band_list')

def band_delete(request, band_id):
  band = Band.objects.get(id=band_id)
  if request.method == 'POST':
    band.delete()
    return redirect('band_list')

  return render(request,
                'listings/band_delete.html',
                {'band': band}
                )

def listing_list(request):
    listings = Listing.objects.all()
    return render(request,
                  'listings/listing_list.html',
                  {'listings': listings}
                  )

def listing_detail(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    listing_dict = model_to_dict(listing)
    return render(request,
                  'listings/listing_detail.html',
                   {'listing': listing_dict}
                  )

def listing_create(request):
  if request.method == 'POST':
    form = ListingForm(request.POST)
    if form.is_valid():
      listing = form.save()
      return redirect('listing_detail', listing_id=listing.id)
  else:
    form = ListingForm()
  return render(request,
                'listings/listing_create.html',
                {'form': form}
                )

def listing_edit(request, listing_id):
  listing = Listing.objects.get(id=listing_id)
  if request.method == 'POST':
    form = ListingForm(request.POST, instance=listing)
    if form.is_valid():
      listing = form.save()
      return redirect('listing_detail', listing_id=listing.id)
  else:
    form = ListingForm(instance=listing)
  return render(request,
                'listings/listing_edit.html',
                {'form': form}
                )

def listing_delete(request, listing_id):
  listing = Listing.objects.get(id=listing_id)
  if request.method == 'POST':
    listing.delete()
    return redirect('listing_list')

  return render(request,
                'listings/listing_delete.html',
                {'listing': listing}
                )

def contact(request):
  print('La méthode de requête est : ', request.method)
  print('Les données POST sont : ', request.POST)
  if request.method == 'POST':
     # créer une instance de notre formulaire et le remplir avec les données POST
    form = ContactUsForm(request.POST)
    if form.is_valid():
      send_mail(
        subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
        message=form.cleaned_data['message'],
        from_email=form.cleaned_data['email'],
        recipient_list=['admin@merchex.xyz'],
      )
    return redirect('email_sent')  # ajoutez cette instruction de retour
    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).
  else:
    # ceci doit être une requête GET, donc créer un formulaire vide
    form = ContactUsForm()
  return render(request,
          'listings/contact.html',
          {'form': form})  # passe ce formulaire au gabarit



def emailConfirm(request):
  return render(request, 'listings/email_confirm.html')

def about(request):
    return render(request, 'listings/about.html')
