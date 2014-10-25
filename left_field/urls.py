from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'left_field.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin', include(admin.site.urls)),
)
urlpatterns += patterns('api.views',
    url(r'^updata$', 'updata'),
    url(r'^newlover$', 'new_lover'),
    url(r'^havelove$', 'have_love'),
)
