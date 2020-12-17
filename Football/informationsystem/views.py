from django.contrib.auth import login, logout
from django.db import connection
from django.forms import Form
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import CustomQueryForm, UserLoginForm
from .models import *


class IndexView(ListView):
    queryset = object
    template_name = 'informationsystem/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home page'
        context['models'] = {
            'Cups': 'caps',
            'Titles': 'titles',
            'Achievements': 'achievements',
            'Players': 'players'}
        return context


class CupsView(ListView):
    Model = Cup
    context_object_name = 'cups'
    template_name = 'informationsystem/cups.html'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cups page'
        return context

    def get_queryset(self):
        return Cup.objects.all()


class TitlesView(ListView):
    Model = Title
    context_object_name = 'titles'
    template_name = 'informationsystem/titles.html'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Titles page'
        return context

    def get_queryset(self):
        return Title.objects.all()


class AchievementsView(ListView):
    Model = Achievement
    context_object_name = 'achievements'
    template_name = 'informationsystem/achievements.html'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Achievements page'
        return context

    def get_queryset(self):
        return Achievement.objects.all()


class PlayersView(ListView):
    Model = Player
    context_object_name = 'players'
    template_name = 'informationsystem/players.html'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Players page'
        return context

    def get_queryset(self):
        return Player.objects.all()


class QueriesView(ListView):
    queryset = object
    template_name = 'informationsystem/queries/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Queries page'
        context['models'] = {
            'Get count of the players': 'get_count_players',
            'Get players by salary': 'get_players_by_salary',
        }
        return context


def get_count_players(request):
    if request.method == 'POST':
        with connection.cursor() as c:
            c.callproc('get_count_players', )
            result = c.fetchall()
        context = {'result': result, 'title': 'Query result'}
        return render(request, 'informationsystem/queries/get_count_players/result.html', context)
    else:
        query_form = Form()
        context = {'form': query_form, 'title': 'Get count of the players'}
        return render(request, 'informationsystem/queries/get_count_players/query.html', context)


def get_players_by_salary(request):
    if request.method == 'POST':
        salary = request.POST.get("salary")
        with connection.cursor() as c:
            c.callproc('get_players_by_salary', [salary])
            results = c.fetchall()
        length = len(results)
        context = {'results': results, 'title': 'Query result', 'length': length}
        return render(request, 'informationsystem/queries/get_players_by_salary/result.html', context)
    else:
        query_form = CustomQueryForm()
        context = {'form': query_form, 'title': 'Get players by salary'}
        return render(request, 'informationsystem/queries/get_players_by_salary/query.html', context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'informationsystem/authorization.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')
