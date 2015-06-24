from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'ask_boldyrev.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^get_params', 'ask_boldyrev.views.show_request_params'),
    url(r'^main', 'ask_boldyrev.views.main'),
    url(r'^questions/', include('questions.urls')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append( 
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
