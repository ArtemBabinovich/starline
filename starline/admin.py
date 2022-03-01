from django.contrib import admin

from starline.models import Comment, Answer_Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'numbers_phone', 'body')
    list_filter = ('name', 'numbers_phone')
    search_fields = ('name', 'numbers_phone', 'pub_data', 'body')


admin.site.register(Comment, CommentAdmin)


class Answer_Comment_Admin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'body', 'pub_data')


admin.site.register(Answer_Comment, Answer_Comment_Admin)
