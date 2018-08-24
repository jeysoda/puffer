from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('favicon.ico/', RedirectView.as_view(
         url=staticfiles_storage.url('puffer/dist/images/favicon.ico')),
         name='favicon'),
    path('profile/', views.profile, name='profile'),
    path('player/', views.player, name='player'),
    path('rating/', views.rating, name='rating'),
    path('monitoring/', views.monitoring, name='monitoring'),
]
