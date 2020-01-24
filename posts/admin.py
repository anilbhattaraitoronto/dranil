from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on', 'topic',
                    'is_archived', 'is_featured')
    list_display_links = ('title',)
    list_filter = ('author', 'topic', 'is_featured', 'is_archived')
    prepopulated_fields = {'slug': ('title',), }


class CommentAdmin(admin.ModelAdmin):
    list_display = ('writer', 'email', 'post', 'posted_on')
    list_display_links = ('post', )


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

# Register your models here.
