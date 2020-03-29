from django.views.generic import ListView
from django.views.generic import DetailView

# Create your views here.
from main1.models import Teams, Tasks


class TeamsView(ListView):
    model = Teams


class TasksView(ListView):
    model = Tasks


class TeamsDetailView(DetailView):
    model = Teams


class TeamsDetail(DetailView):
    model = Teams

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['participants_list'] = Teams.get
        return context
