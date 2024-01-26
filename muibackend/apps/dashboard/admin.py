from django.contrib import admin
#from .models import venue
#from .models import MyClubsUser
#from .models import Event
from .models import Item


admin.site.register(Item)

#admin.site.register(MyClubsUser)

#admin.register(venue)
#class VenueAdmin(admin.ModelAdmin):
#    list_display = ('name', 'address')
 #   ordering = ('name')
  #  search_fields = ('name', 'address')

#admin.register(Event)
#class VenueAdmin(admin.ModelAdmin):
 #   Fields = ('name', 'venue', 'event_date')
  #  list_display = ('name', 'event_date')
   # list_filter = ('venue', 'event_date')
    #ordering = ('event_date')
from .models import Konsultasi
from .models import Gallery

admin.site.register(Konsultasi)
admin.site.register(Gallery)
