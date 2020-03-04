from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from django.utils.safestring import mark_safe
from .models import (Post,BigCategory,SmallCategory)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_preview', 'card_text', 'is_public', 'created_date')
    ordering = ('-created_date',)
    list_filter = ('is_public',)
    search_fields = ('title', 'card_text')

    def thumbnail_preview(self, obj):
        return mark_safe('<img src="{}" style="width:100px; height:auto;">'.format(obj.thumbnail.url))

    thumbnail_preview.short_description = 'プレビュー'


class ListView(PostAdmin, MarkdownxModelAdmin):
    pass

# Register your models here.
admin.site.register(Post, ListView)
admin.site.register(BigCategory,)
admin.site.register(SmallCategory)






