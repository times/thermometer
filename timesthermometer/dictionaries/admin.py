from django.contrib import admin
from timesthermometer.dictionaries.models import Positive, Negative, Incrementer, Decrementer, Inverter

class PositiveAdmin(admin.ModelAdmin):
  list_display = ('label',)
  search_fields = ('label',)
  list_per_page = 50
  list_max_show_all = 1000

class NegativeAdmin(admin.ModelAdmin):
  list_display = ('label',)
  search_fields = ('label',)
  list_per_page = 50
  list_max_show_all = 1000

class IncrementerAdmin(admin.ModelAdmin):
  list_display = ('label',)
  search_fields = ('label',)
  list_per_page = 50
  list_max_show_all = 1000

class DecrementerAdmin(admin.ModelAdmin):
  list_display = ('label',)
  search_fields = ('label',)
  list_per_page = 50
  list_max_show_all = 1000

class InverterAdmin(admin.ModelAdmin):
  list_display = ('label',)
  search_fields = ('label',)
  list_per_page = 50
  list_max_show_all = 1000

admin.site.register(Positive, PositiveAdmin)
admin.site.register(Negative, NegativeAdmin)
admin.site.register(Incrementer, IncrementerAdmin)
admin.site.register(Decrementer, DecrementerAdmin)
admin.site.register(Inverter, InverterAdmin)

from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)