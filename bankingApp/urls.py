
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from userauths import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("core.urls")),
    path("user/", include("userauths.urls")),
    path("accounts/", include("userauths.urls")),
    path("account/", include("account.urls")),
    # path("accounts/login",  views.LoginView, name="sign-in"),
    path('', include('django.contrib.auth.urls'))
   
]


if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)