from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
#from modelTest import settings
from django.utils.html import format_html
#from .widgets import BooleanButtonWidget
import os

class MediafileInline(admin.TabularInline):
#    formfield_overrides = {
#        models.BooleanField: {'widget': BooleanButtonWidget },
#    }
    model = Mediafile
    extra = 1
    readonly_fields = ('image_tag',)


class CharacteristicInline(admin.TabularInline):
    model = Characteristic
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name'),
    exclude = ['alias']
    inlines = [
        MediafileInline,
        CharacteristicInline,
    ]
    ordering = ('name',)
    list_filter = ('category', )

class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'name_uk', 'meta_keywords', 'meta_description', 'full_description', 'full_description_uk', 'children', 'image', 'image_tag')

    readonly_fields = ('image_tag',)


class ProjectAdmin(admin.ModelAdmin):
    fields = ('name', 'name_uk', 'description', 'description_uk', 'image', 'image_tag')
    readonly_fields = ('image_tag',)




admin.site.register(Project, ProjectAdmin)
#admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CharacteristicName)
admin.site.register(Brand)


#admin.site.register(Comments)

