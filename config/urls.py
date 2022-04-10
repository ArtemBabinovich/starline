from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from starline import views

router = routers.DefaultRouter()
router.register(r'comments', views.CommentViewSet)
router.register(r'popular_product', views.PopularProductViewSet)
router.register(r'novelties_product', views.NoveltiesProductViewSet)
router.register(r'our_work', views.OurWorkViewSet)
router.register(r'category_search', views.CategotyFiltViewSet)
router.register(r'category_work', views.CategoryWorkViewSet)

app_name = 'starline'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('starline.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('starline/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
