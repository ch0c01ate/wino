from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from images.views import *

urlpatterns = [
    path('image_upload', image_view, name='image_upload'),
    path('success', success, name='success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)