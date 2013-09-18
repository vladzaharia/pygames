from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.views import generic
from gamesapp.models import Game

class IndexView(generic.ListView):
	template_name = 'index.html'
	context_object_name = 'game_list'
	model = Game

	def get_queryset(self):
		"""Return all games."""
		return Game.objects.all()

class DetailView(generic.DetailView):
	template_name = 'game.html'
	model = Game

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(DetailView, self).get_context_data(**kwargs)
		# Add in a Likes/Dislikes/Owners
		game = self.get_object()

		context['player_same'] = game.min_players == game.max_players
		context['has_platform'] = game.game_type == 'Console'
		context['likes'] = game.gamepreference_set.filter(preference='Like')
		context['dislikes'] = game.gamepreference_set.filter(preference='Dislike')
		context['owners'] = list(game.gamecopy_set.all())
		return context

class TypeFilterView(generic.ListView):
	template_name = 'index.html'
	context_object_name = 'game_list'
	model = Game

	def get_queryset(self):
		"""Return all games."""
		return Game.objects.filter(game_type=self.kwargs['game_type'])

class PlatformFilterView(generic.ListView):
	template_name = 'index.html'
	context_object_name = 'game_list'
	model = Game

	def get_queryset(self):
		"""Return all games."""
		return Game.objects.filter(platform=self.kwargs['platform'])