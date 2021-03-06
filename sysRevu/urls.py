from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

		
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'newProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sysrev/', include('sysrev.urls')),
    url(r'^', include('sysrev.urls')),
   	#url(r'^accounts/',include('registration.backends.simple.urls')),
)
# UNDERNEATH your urlpatterns definition, add the following two lines:
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
