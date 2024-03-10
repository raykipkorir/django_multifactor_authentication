from django.contrib import admin
from django.urls import include, path
from two_factor.urls import urlpatterns as tf_urls

from accounts.views import my_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(tf_urls)),
    path("index/", my_view)
]
