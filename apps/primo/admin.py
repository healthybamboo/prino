from django.contrib import admin
from django.utils.html import mark_safe
from .models import Category, Movie
from django.forms import Select, TextInput, ModelForm


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'end_at',
        'is_active',
        'status',
        'episode',
        'episode_title',
        'preview',
    )

    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            self.exclude = [
                'status',
                'title',
                'image',
                'episode',
                'episode_title',
                'end_at',
                'is_active',
            ]
        return super().get_form(request, obj, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        if obj is None:
            return []
        return ['status', 'title', 'image', 'episode', 'episode_title', 'url']

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image}" width="150px" />')
