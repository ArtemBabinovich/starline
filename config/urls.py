from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from starline import viewsAPI


router = routers.DefaultRouter()
router.register(r'comments', viewsAPI.CommentViewSet)
router.register(r'popular_product', viewsAPI.PopularProductViewSet)
router.register(r'our_work', viewsAPI.OurWorkViewSet)
router.register(r'category_search', viewsAPI.CategotyFiltViewSet)
router.register(r'novelties', viewsAPI.NoveltiesProductViewSet)
router.register(r'product', viewsAPI.ProductViewSet)
router.register(r'all_category', viewsAPI.CategoryViewSet)
router.register(r'characteristic', viewsAPI.CharacteristicSerializerViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('starline.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('starline/', include(router.urls)),
]

handler404 = 'starline.views.error'
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
