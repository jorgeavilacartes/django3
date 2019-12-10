''' 
__author__      =       "Roberto Rocuant" 
__version__     =       "1.0" 
__created__     =       "12/07/2019 01:05" 
''' 
 

from .views import (
    ColorCreateView,
    ColorDeleteView,
    ColorDetailView,
    ColorFormView,
    ColorListView,
    ColorTemplateView,
    ColorUpdateView,
    HomeTemplateView,
    SimpleRedirectView,
    SimpleView,
)
from django.contrib import admin 
from django.urls import path
 
 
urlpatterns = [ 
 
    path(
        '',
        HomeTemplateView.as_view(),
        name = "home",
    ), 
    path(
        'colors',
        ColorTemplateView.as_view(),
        name = "colors",
    ), 
    path(
        'colors/list',
        ColorListView.as_view(),
        name = "colorslist"
    ),
    path(
        'colors/detail/<color_id>',
        ColorDetailView.as_view(),
        name = "colorsdetail"
    ),
    path(
        'colors/form',
        ColorFormView.as_view(),
        name = "colorsform"
    ),
    path(
        'colors/create',
        ColorCreateView.as_view(),
        name = "colorscreate"
    ),
    path(
        'colors/detail/<color_id>/update',
        ColorUpdateView.as_view(),
        name = "colorsupdate"
    ),
    path(
        'colors/detail/<color_id>/delete',
        ColorDeleteView.as_view(),
        name = "colorsdelete"
    ),
    path(
        'simpleview',
        SimpleView.as_view(),
        name = "simpleview"
    ),
    path(
        'simpleredirectview',
        SimpleRedirectView.as_view(),
        name = "simpleredirectview"
    ),
] 