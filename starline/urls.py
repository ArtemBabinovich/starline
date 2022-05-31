from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import all_product, DetailProductView, ActionView, \
    listourwork, index, ContactsView, AboutCompanyView, DetailOurWorkView, not_page

urlpatterns = [
    path('', index, name='index'),
    path('contact/', ContactsView.as_view(), name='contact'),
    path('about_company/', AboutCompanyView.as_view(), name='about_company'),
    path('action/', ActionView.as_view(), name='action'),
    path('our_works/', listourwork, name='our_works'),
    path('our_work/<slug:slug>/', DetailOurWorkView.as_view(), name='detail_ourwork_view'),
    path('catalog/', all_product, name='catalog'),
    path('catalog/product/<slug:slug>/', DetailProductView.as_view(), name='detail_product_view'),
    path('not_page/', not_page, name='error'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
