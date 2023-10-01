from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings #allows access to MEDIA_URL and MEDIA_ROOT
from django.conf.urls.static import static # helper function; create URLs from local folder names

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("recipes.urls"))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



