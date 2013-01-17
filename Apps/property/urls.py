__author__ = 'aamirhussain'
from django.conf.urls import patterns, include, url
from views import HomePageView

urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(), name='HomePage'),
)
