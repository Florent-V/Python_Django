# listings/forms.py

from django import forms
from listings.models import Band, Listing

class ContactUsForm(forms.Form):
   name = forms.CharField(required=False)
   email = forms.EmailField()
   message = forms.CharField(max_length=1000)
  
# class BandForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     genre = forms.ChoiceField(choices=[('HH', 'Hip Hop'), ('SP', 'Synth Pop'), ('AR', 'Alternative Rock')])
#     biography = forms.CharField(max_length=1000)
#     year_formed = forms.IntegerField(min_value=1900, max_value=2021)
#     active = forms.BooleanField(required=False)
#     official_homepage = forms.URLField(required=False)

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        #fields = ['name', 'genre', 'biography', 'year_formed', 'active', 'official_homepage']
        #fields = '__all__'
        exclude = ('active', 'official_homepage')  # ajoutez cette ligne

class ListingForm(forms.ModelForm):
    band = forms.ModelChoiceField(queryset=Band.objects.filter(active=True))
    class Meta:
        model = Listing
        #fields = ['name', 'genre', 'biography', 'year_formed', 'active', 'official_homepage']
        fields = '__all__'
        #exclude = ('active', 'official_homepage')  # ajoutez cette ligne


# formulaire pour la création d'une annonce
# class ListingForm(forms.Form):
#     title = forms.CharField(max_length=100)
#     description = forms.CharField(max_length=1000)
#     price = forms.IntegerField(min_value=0)
#     photo = forms.ImageField(required=False)
#     # ajoutez ce champ
#     band = forms.ModelChoiceField(queryset=Band.objects.all())
    # ajoutez ce champ
    #city = forms.ModelChoiceField(queryset=City.objects.all())
    # ajoutez ce champ
    #category = forms.ModelChoiceField(queryset=Category.objects.all())
    # ajoutez ce champ
    #user = forms.ModelChoiceField(queryset=User.objects.all())
    # ajoutez ce champ
    #created_at = forms.DateTimeField()
    # ajoutez ce champ
    #updated_at = forms.DateTimeField()
    # ajoutez ce champ
    #active = forms.BooleanField()
    # ajoutez ce champ
    #slug = forms.SlugField(max_length=100)
