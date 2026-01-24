from django.contrib import admin

# Register your models here.
from .models import (
    Language, Guide,
    GuidePost,
    GuidePostImage,
    Tour
)

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    # Fields to display in list view
    list_display = ('name', 'code')
    
    # Add search box (searches in these fields)
    search_fields = ('name', 'code')
    
    # Optional: add ordering
    ordering = ('-name',)

@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    # Fields to display in list view
    list_display = ('name', 'bio')
    
    # Add search box (searches in these fields)
    search_fields = ('name', 'code', 'lang')
    
    # Add filters on the right side
    list_filter = ('lang','created_at')
    
    # Optional: add ordering
    ordering = ('name',) 

    def short_bio(self, obj):
        return obj.bio[:50] + '...'
    
@admin.register(GuidePost)
class GuidePostAdmin(admin.ModelAdmin):
    # Fields to display in list view
    list_display = ('guide', 'short_title', 'short_content', 'created_at',)
    
    # Add search box (searches in these fields)
    search_fields = ('short_title',)
    
    # Add filters on the right side
    list_filter = ('created_at',)
    
    # Optional: add ordering
    ordering = ('-created_at',) 

    def short_title(self, obj):
        return obj.title[:50] + '...'
    
    def short_content(self, obj):
        return obj.content[:50] + '...'
    
@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    # Fields to display in list view
    list_display = ('guide', 'short_title', 'price', 'short_desc', 'created_at',)
    
    # Add search box (searches in these fields)
    search_fields = ('title', 'price')
    
    # Add filters on the right side
    list_filter = ('price', 'created_at')
    
    # Optional: add ordering
    ordering = ('-created_at',) 

    def short_title(self, obj):
        return obj.title[:50] + '...'
    
    def short_desc(self, obj):
        return obj.description[:50] + '...'
    
admin.site.register(GuidePostImage)