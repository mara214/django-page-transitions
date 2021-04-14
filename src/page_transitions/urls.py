from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
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
    path('', TemplateView.as_view(template_name='pages/index.html')),
    path('a/', TemplateView.as_view(template_name='pages/a.html')),
    path('b/', TemplateView.as_view(template_name='pages/b.html')),
]