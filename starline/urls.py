from django.urls import path

from .views import contact, feedb, layout, CatalogView, AllProductView, DetailProductView, CommentView

urlpatterns = [
    path('', layout, name='layout'),
    path('register/', CommentView.as_view(), name='comment'),
    path('contacts/', contact, name='contacts'),
    path('feedback/', feedb, name='feedback'),
    path('catalog/', CatalogView.as_view(), name='catalog_view'),
    path('catalog/<str:cat_slug>/', AllProductView.as_view(), name='all_product_view'),
    path('catalog/<str:cat_slug>/<str:prod_slug>/', DetailProductView.as_view(), name='detail_product_view')
]
