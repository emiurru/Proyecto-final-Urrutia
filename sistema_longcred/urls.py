from django.contrib import admin
from django.urls import path, include
from .views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('app-creditos/', include('app_creditos.urls'))
]
