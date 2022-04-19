from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import CatalogView, AllProductView, DetailProductView, ActionView, \
    OurWorkView, index, ContactsView, AboutCompanyView

urlpatterns = [
    path('', index, name='index'),
    path('contact/', ContactsView.as_view(), name='contact'),
    path('about_company/', AboutCompanyView.as_view(), name='about_company'),
    path('catalog/', CatalogView.as_view(), name='catalog_view'),
    path('action/', ActionView.as_view(), name='action'),
    path('our_work/', OurWorkView.as_view(), name='our_work'),
    path('catalog/<str:cat_slug>/', AllProductView.as_view(), name='all_product_view'),
    path('catalog/<str:cat_slug>/<str:prod_slug>/', DetailProductView.as_view(), name='detail_product_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
