from django.contrib import admin
from django.urls import path, include
from proyectos.views import index, search_all
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("plantel/", include("plantel.urls")),
    path("notes/", include("blog.urls")),
    path("selecciones/", include("selecciones.urls")),
    path("groups/", include("groups.urls")),
    path("estadios/", include("estadios.urls")),
    path("users/", include("users.urls")),
    path("search/", search_all, name="search"),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
