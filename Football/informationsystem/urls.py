from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('caps/', CupsView.as_view(), name='caps'),
    path('titles/', TitlesView.as_view(), name='titles'),
    path('achievements/', AchievementsView.as_view(), name='achievements'),
    path('players/', PlayersView.as_view(), name='players'),
    path('queries/', QueriesView.as_view(), name='queries'),
    path('queries/1', get_count_players, name='get_count_players'),
    path('queries/2', get_players_by_salary, name='get_players_by_salary'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
