from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_title = 'Floor Tajima'
admin.site.site_header = 'Floor Tajima'
admin.site.index_title = 'メニュー'

urlpatterns = [
    path('tajima/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
