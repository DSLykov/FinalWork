from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import (
    obtain_auth_token,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("posts.urls")),
    path("api-token-auth/", obtain_auth_token),
    path("", RedirectView.as_view(url="/api/posts/")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
