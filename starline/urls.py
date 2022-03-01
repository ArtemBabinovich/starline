from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from starline.views import contact, feedb

urlpatterns = [
    path('contacts/', contact, name='contacts'),
    # path('feedback/', MyView.as_view(), name='feedback'),
    path('feedback/', feedb, name='feedback'),

]
