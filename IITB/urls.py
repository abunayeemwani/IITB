from django.contrib import admin
from django.urls import path, include
from api.routers import router

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
]
