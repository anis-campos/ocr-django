from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.listing),
    path('search/', views.search),
    re_path(r'^(?P<album_id>[0-9]{1,2})/$', views.detail),

]
