from django.conf.urls import patterns, include, url

from django.contrib import admin
from mysite.views import hello
from mysite.views import current_datetime
from mysite.views import hours_ahead
from mysite.views import display_request_info
from mysite.views import display_request_info_tpl
from mysite.views import search_form
from mysite.views import search
from mysite.contact.views import contact
from mysite.tables.views import people
from mysite.ADAdmin.views import upload_file, process

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
		url('^hello/$', hello),
		#url('^time/$', current_datetime),
		#url(r'^time/plus/(\d{1,2})/$', hours_ahead),
		#url('^meta_info/$', display_request_info),
		#url('^meta_info_tpl/$', display_request_info_tpl),
		#url('^search_form/$', search_form),
		#url('^search/$', search),
		#url('^contact/$', contact),
    url('^upload/$', upload_file),
    url('^process/$', process),
    #url('^people/$', people),
)
