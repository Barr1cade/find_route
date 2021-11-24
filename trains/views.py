from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from trains.models import Train

__all__ = (
    'home', 'TrainDetailView',
)


def home(request, pk=None):
    qs = Train.objects.all()
    context = {'objects_list': qs}
    return render(request, 'trains/home.html', context)


class TrainListView(ListView):
    model = Train
    template_name = 'trains/home.html'


class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    template_name = 'trains/detail.html'
