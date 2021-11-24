from django.contrib import admin
from django.urls import path, include

from travel.views import home, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trains/', include(('trains.urls', 'trains'))),
    path('cities/', include(('cities.urls', 'cities'))),
    path('', home, name='home'),
    path('about/', about),
]
