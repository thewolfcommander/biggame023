from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'jackpot'

urlpatterns = [
	path('', views.home, name='home'),
] 
urlpatterns += static(settings.SOUND_URL, document_root = settings.SOUND_ROOT)