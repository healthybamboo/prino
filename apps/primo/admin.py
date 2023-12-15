from django.contrib import admin
from django.utils.html import mark_safe
from .models import Category, Movie, Log


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

    def get_readonly_fields(self, request, obj=None):
        if obj is None:
            return []
        return ['status', 'title', 'image']

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image}" width="150px" />')

    pass


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = (
        'message',
        'created_at',
    )
