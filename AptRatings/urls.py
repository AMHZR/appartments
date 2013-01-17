from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from ajax_select import urls as ajax_select_urls

admin.autodiscover()
from django.conf import settings
urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('property.urls')),
    # url(r'^AptRatings/', include('AptRatings.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #Admin Tools Urls
    url(r'^admin_tools/', include('admin_tools.urls')),
    #Ajax select urls
    url(r'^admin/lookups/', include(ajax_select_urls)),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG :
    urlpatterns += patterns("django.views",
        url(r'^static_media(?P<path>.*)/$',
            "static.serve", {
                "document_root": settings.MEDIA_ROOT,
                })
    )

