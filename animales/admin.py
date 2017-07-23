from django.contrib import admin
from .models import Animal

@admin.register(Animal)
class AnimalesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'edad', 'especie',)
    list_editable = ('edad', 'especie')
    list_display_links = ('id', 'nombre',)
    list_filter = ('especie',)
    search_fields = ('nombre', 'especie')
