from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   # url(r'^login$',""),
  #  url(r'^logout',""),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tweet/(.*)$', "feedexpander.views.tweet"),
    url(r'^(.*)$', "feedexpander.views.NotFound"),
)
