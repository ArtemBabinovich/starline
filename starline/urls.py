from django.urls import path

from .import views
from .views import layout, CatalogView, AllProductView, DetailProductView, CommentView, FeedbackView

urlpatterns = [
    path('', layout, name='layout'),
    path('register/', CommentView.as_view(), name='comment'),
    path('contacts/', views.СontactsView.as_view(), name='contacts'),
    path('feedback/', FeedbackView.as_view(), name='feedback'),
    # path('feedback/', get_feadback, name='feedback'),

    path('catalog/', CatalogView.as_view(), name='catalog_view'),
    path('catalog/<str:cat_slug>/', AllProductView.as_view(), name='all_product_view'),
    path('catalog/<str:cat_slug>/<str:prod_slug>/', DetailProductView.as_view(), name='detail_product_view')
]
