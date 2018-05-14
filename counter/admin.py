from django.contrib import admin

from .models import Poster
# Register your models here.
class PosterAdmin(admin.ModelAdmin):
    pass

admin.site.register(Poster,PosterAdmin)
