from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('apps.user.urls')),
    path('api/landing-page/', include('apps.landing_page.urls')),
    
]
