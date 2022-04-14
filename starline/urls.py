from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import layout, CatalogView, AllProductView, DetailProductView, CommentView, ActionView, \
    OurWorkView, index, ContactsView

urlpatterns = [
    path('', index),
    path('1/', layout, name='layout'),
    path('register/', CommentView.as_view(), name='comment'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('catalog/', CatalogView.as_view(), name='catalog_view'),
    path('action/', ActionView.as_view(), name='action'),
    path('our_work/', OurWorkView.as_view(), name='our_work'),
    path('catalog/<str:cat_slug>/', AllProductView.as_view(), name='all_product_view'),
    path('catalog/<str:cat_slug>/<str:prod_slug>/', DetailProductView.as_view(), name='detail_product_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
