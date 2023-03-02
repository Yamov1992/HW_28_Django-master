
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cat/', include('ads.urls.categories')),
    path('ads/', include ('ads.urls.ads')),
    path('user/', include('users.urls.user')),
]
