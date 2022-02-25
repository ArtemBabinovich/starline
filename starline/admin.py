from django.contrib import admin

from starline.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'numbers_phone', 'body')
    list_filter = ('name', 'numbers_phone')
    search_fields = ('name', 'numbers_phone', 'pub_data', 'body')


admin.site.register(Comment, CommentAdmin)
