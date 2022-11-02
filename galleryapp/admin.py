from django.contrib import admin

from galleryapp.models import Gallery, Slider

# Register your models here.

class GalleryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


admin.site.register(Gallery,GalleryAdmin)
admin.site.register(Slider)