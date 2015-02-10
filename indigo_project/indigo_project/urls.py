from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'indigo_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'example.views.home', name='home'),
    url(r'^(?P<template_name>[\w-]+.html)$', 'example.views.template', name='template'),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
