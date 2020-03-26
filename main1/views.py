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


class AdminTeamView(ListView):
    model = Teams
