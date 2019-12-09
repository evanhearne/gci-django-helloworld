from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('googlecodein/', include('googlecodein.urls')),
    path('admin/', admin.site.urls),
]