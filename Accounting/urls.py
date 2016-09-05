from Apps.BaseData import CounterParty
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from Accounting import settings
from Apps.Index import MainPage

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
    url(r'^$', MainPage.index_page),
    url(r'^index.html', MainPage.index_page),
                       # url(r'^blog/', include('blog.urls')),
    url(r'^ajax/grid/actualCounterParty/', CounterParty.CounterParty.actual_counterparty_list_maker, ''),
    url(r'^ajax/grid/counterGroup/', CounterParty.CounterParty.counter_group_maker, '')
                       ) + static(settings.STATIC_URL, document_root=settings.STATIC_URL)



urlpatterns += staticfiles_urlpatterns()