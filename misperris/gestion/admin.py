from django.contrib import admin
from .models import Dueño, Mascota

# Register your models here.

admin.site.register(Dueño)
admin.site.register(Mascota)


class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'bio', 'web')
