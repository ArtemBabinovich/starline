from django.contrib import admin
from starline.models import Contacts#, Feedback


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('address', 'time_work1', 'time_work2', 'phone1', 'phone2', 'phone_service')
    list_display_links = ('address',)
    list_editable = ('time_work1', 'time_work2')


# class FeedbackAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'phone', 'message', 'published')
#     search_fields = ('name', 'phone')
#     list_editable = ('published',)


# admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Contacts, ContactsAdmin)
# admin.site.register(Feedback)
