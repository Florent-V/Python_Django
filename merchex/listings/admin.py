from django.contrib import admin

from listings.models import Band, Listing

class BandAdmin(admin.ModelAdmin):
  list_display = ('name', 'genre', 'year_formed', 'active')
  list_filter = ('genre', 'active')
  search_fields = ('name', 'genre', 'year_formed', 'active')

class ListingAdmin(admin.ModelAdmin):
  list_display = ('title', 'year', 'price', 'sold', 'type')
  list_filter = ('year', 'price', 'sold')
  search_fields = ('title', 'year', 'price', 'sold')

admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)
