from django.contrib import admin
from django.utils.safestring import mark_safe
from starline.models import Comment, Contacts, Category, Product, Feedback, Action, OurWork, Security, Characteristic, \
    Company


class SecurityAdmin(admin.ModelAdmin):
    list_display = ('title',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'published')
    exclude = ('slug',)
    list_display_links = ('title',)
    list_editable = ('published',)


class CharecteristicAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


class ProductAdmin(admin.ModelAdmin):
    list_per_page = 20
    exclude = ('slug',)
    list_display = (
        'title',
        'price',
        'price_install',
        'image_img',
        'presence',
        'published',
        'popular',
        'novelties'
    )
    list_display_links = ('title',)
    list_editable = ('price', 'price_install', 'presence', 'popular', 'novelties', 'published')

    def image_img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="80" height="80">')
        else:
            return 'Нет изображения'

    image_img.short_description = 'Изображение'


class ActionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'published')
    list_display_links = ('title',)
    list_editable = ('published',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'numbers_phone', 'body_reduction', 'published')
    list_editable = ('published',)
    list_filter = ('title', 'name', 'numbers_phone')
    search_fields = ('title', 'name', 'numbers_phone', 'pub_data', 'body_reduction')


class OurWorkAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'installation_time',
        'installation_price',
        'image1',
        'published',
    )
    exclude = ('slug',)
    list_filter = ('title',)
    list_display_links = ('title',)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'message', 'published')
    list_filter = ('published',)
    list_editable = ('published',)


class ContactsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'address',
        'phone1',
        'phone2',
        'email',
        'time_work1',
        'time_work2',
    )
    list_display_links = ('name',)
    list_editable = ('time_work1', 'time_work2')


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('description', 'image1', 'image2', 'image3')
    list_display_links = ('description',)


admin.site.register(Company, CompanyAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Action, ActionAdmin)
admin.site.register(OurWork, OurWorkAdmin)
admin.site.register(Security, SecurityAdmin)
admin.site.register(Characteristic, CharecteristicAdmin)
