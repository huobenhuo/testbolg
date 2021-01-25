from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^hello_world/',views.hello_world),
    url(r'^article_content/',views.article_content),
    url(r'^index/',views.get_index_page),
    url(r'^detail/(?P<article_id>[0-9]+)/$',views.get_detail_page),
]