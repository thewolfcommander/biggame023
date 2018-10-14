from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('admin/', admin.site.urls, name='admin'),
    path('our-games/', views.our_games, name='our_games'),
    path('contact-us/', views.contact, name = 'contact'),
    path('support/', views.support, name = 'support'),
    path('help/', views.help, name = 'help'),
    path('total-rewards/', views.rewards, name = 'rewards'),
    path('demo/', views.demo, name = 'demo'),
    path('get-started/', views.get_started, name = 'get_started'),
    path('not-found-error/', views.show404, name='show404'),
    path('internal-server-error/', views.show500, name='show500'),
    path('promotion/', views.promotion, name = 'promotion'),
    path('my-profile/<pk>/', views.my_profile, name='my_profile'),
    path('settings/<pk>/', views.user_set, name='user_set'),
    path('add-profile/<pk>/', views.add_profile, name='add_profile'),
]