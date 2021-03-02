"""CMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from backend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('htmles/', views.index_htmles),
    path('htmles/add_data/', views.add_div_id),
    path('htmles/add_header/', views.add_header_id),
    path('bodys/<int:elementid>/', views.index_bodys),
    path('bodys/delete_id/', views.delete_body_id),
    path('dives/<int:elementid>/', views.index_dives),
    path('dives/delete_id/', views.delete_div_id),
    path('htmles/create/', views.create_htmles),
    path('htmles/create_html/', views.create_htmles),
    path('bodys/create/<int:elementid>/', views.create_bodys),
    path('dives/create/<int:elementid>/', views.create_dives),
    path('favicon.ico', RedirectView.as_view(url='/static/img/termidesk_ico.png')),
]
