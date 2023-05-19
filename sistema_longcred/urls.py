from django.contrib import admin
from django.urls import path, include
from .views import inicio

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('app-creditos/', include('app_creditos.urls')),
    path('perfiles/', include('perfiles.urls'))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
