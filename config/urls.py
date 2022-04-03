from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from starline import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

app_name = 'starline'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('starline.urls')),
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
