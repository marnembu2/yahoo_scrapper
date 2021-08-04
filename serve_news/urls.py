from . import views as views
from django.conf.urls import include, url


urlpatterns = [
    url(r'^$', views.news),
]
