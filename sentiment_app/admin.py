from django.contrib import admin
from .model.models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'sentiment', 'confidence', 'created_at')
