from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'better.views.home', name='home'),
    url(r'^login', 'better.views.user_login', name='user_login'),
    url(r'^logout','better.views.user_logout',name='user_logout'),
    url(r'^signup','better.views.signup',name="signup"),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^signup/', include('signups.urls', namespace= "signups")),
    #url(r'^polls/',include('polls.urls', namespace="polls")),
url(r'^admin/', include(admin.site.urls)),
)
