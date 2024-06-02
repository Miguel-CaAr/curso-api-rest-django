from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-admin/', include("api_admin.urls")),
    path('auth/', include('api_auth.urls')),
    path('', include("pos.urls")),
]
