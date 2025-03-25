from django.contrib import admin
from django.urls import path
from. import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('india/', views.india, name = 'india'),
    path('detail/<int:id>/', views.detail, name = 'detail'),
    path('search/', views.search, name = 'search'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
