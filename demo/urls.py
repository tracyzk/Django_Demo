"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

	url(r'^add/$', 'article.views.add'),
	url(r'^manage/$', 'article.views.manage'),
	url(r'^del/(?P<id>[\d]+)$', 'article.views.delete'),
	url(r'^modify/(?P<id>[\d]+)$', 'article.views.modify'),
	url(r'^modify_handle/$', 'article.views.modify_handle'),

	url(r'^$', 'home.views.list'),
	url(r'^list/$', 'home.views.list'),
	url(r'^search/$', 'home.views.search'),
	url(r'^show/(?P<id>[\d]+)$', 'home.views.show'),
	


	url( r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': settings.STATIC_ROOT }),  
]
