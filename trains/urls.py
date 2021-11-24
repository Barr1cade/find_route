from django.urls import path

from trains.views import *

urlpatterns = [
    path('', home, name='home'),
    # path('', TrainListView.as_view(), name='home'),
    path('detail/<int:pk>/', TrainDetailView.as_view(), name='detail'),
]
