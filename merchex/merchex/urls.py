"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from listings import views
from django.conf import settings
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bands/', views.band_list, name='band_list'),
    path('bands/<int:band_id>/', views.band_detail, name='band_detail'),
    path('bands/add/', views.band_create, name='band_create'),
    path('bands/<int:band_id>/edit/', views.band_edit, name='band_edit'),
    path('bands/<int:band_id>/delete/', views.band_delete, name='band_delete'),
    path('about-us/', views.about, name='about_us'),
    path('contact-us/', views.contact, name='contact'),
    path('email-confirm/', views.emailConfirm, name='email_sent'),
    path('listings/', views.listing_list, name='listing_list'),
    path('listings/<int:listing_id>/', views.listing_detail, name='listing_detail'),
    path('listings/add/', views.listing_create, name='listing_create'),
    path('listings/<int:listing_id>/edit/', views.listing_edit, name='listing_edit'),
    path('listings/<int:listing_id>/delete/', views.listing_delete, name='listing_delete'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns