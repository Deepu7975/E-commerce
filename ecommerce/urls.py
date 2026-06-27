from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView   # ← add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/core/home/')),  # ← add this
    path('core/', include('core.urls')),
    path('account/', include('account.urls')),
    path('sellar/', include('sellar.urls')),
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)