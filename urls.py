from django.conf.urls.defaults import *
from django.contrib import admin
import server, settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', server.views.list),
    (r'^schedule$', server.views.schedule),
    (r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)

