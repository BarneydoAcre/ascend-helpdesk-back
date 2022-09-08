from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('suport.urls')),
    path('', include('default.urls')),
    path('foodservice/', include('foodservice.urls')),
]
