from django.conf.urls.static import static
from django.urls import path

from ConstrWebsite import settings

from . import views


app_name = 'core'
urlpatterns = [
    path('', views.MainView.as_view()),
    path('fontains/', views.FountainsView.as_view()),
    path('pools/',views.PoolsView.as_view()),
    path('baths/',views.BathView.as_view()),
    path('spa/',views.SPAView.as_view()),
    path('hummum/',views.HummumView.as_view()),
    path('autowat/',views.AutowatView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

