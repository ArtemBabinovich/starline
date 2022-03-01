from django.contrib import admin
from starline.models import Contacts#, Feedback
from starline.models import Comment, Answer_Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'numbers_phone', 'body')
    list_filter = ('name', 'numbers_phone')
    search_fields = ('name', 'numbers_phone', 'pub_data', 'body')


class Answer_Comment_Admin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'body', 'pub_data')



class ContactsAdmin(admin.ModelAdmin):
    list_display = ('address', 'time_work1', 'time_work2', 'phone1', 'phone2', 'phone_service')
    list_display_links = ('address',)
    list_editable = ('time_work1', 'time_work2')
    

admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Answer_Comment, Answer_Comment_Admin)