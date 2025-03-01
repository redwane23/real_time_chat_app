from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include('home.urls')),
    path('auth/',include("authontication.urls")),
    path('api/',include("api.urls")),
    path('silk/', include('silk.urls', namespace='silk')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)