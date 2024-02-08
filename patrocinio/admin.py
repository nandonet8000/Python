from django.contrib import admin

from patrocinio.models import Patrocinio

class Listando(admin.ModelAdmin):
  

    list_per_page = 10

admin.site.register(Patrocinio, Listando)
