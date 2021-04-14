from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve


urlpatterns = []


if settings.DEBUG:
    urlpatterns += [
        url(
            r'^%s(?P<path>.*)$' % settings.MEDIA_URL.strip('/'),
            serve, {'document_root': settings.MEDIA_ROOT}
        ),
    ]


urlpatterns += [
    url(r'^admin/', admin.site.urls),
]