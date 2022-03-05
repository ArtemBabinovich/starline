from django.contrib import admin
from starline.models import Comment, Answer_Comment, Contacts, Category, Product, Feedback


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


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'published')
    exclude = ('slug',)
    list_display_links = ('title',)
    list_editable = ('published',)


class ProductAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('title', 'price', 'price_install', 'time_first', 'time_second', 'published')
    list_display_links = ('title',)
    list_editable = ('price', 'price_install', 'published')


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'message', 'published')
    list_filter = ('published',)
    list_editable = ('published',)


admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Answer_Comment, Answer_Comment_Admin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Feedback, FeedbackAdmin)
