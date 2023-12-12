from django.contrib import admin

from ads.models import Ad, Comment

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')
    search_fields = ('discription',)
    list_filter = ('created_at',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'ad')