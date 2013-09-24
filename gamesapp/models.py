from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import UUIDField

# Information about a Game
class Game(models.Model):
	TYPE_CHOICES = (
		('Board', 'Board Game'),
		('Card', 'Card Game'),
		('Console', 'Console Game'))
	PLATFORM_CHOICES = (
		('PS3', 'Playstation 3'),
		('X360', 'Xbox 360'),
		('Wii', 'Wii'),
		('GC', 'GameCube'),
		('NDS', 'Nintendo 3DS'),
		('PSV', 'Playstation Vita'),
		('None', 'None'))

	name = models.CharField(max_length=50, verbose_name=u'Name')
	game_type = models.CharField(max_length=10, choices=TYPE_CHOICES, verbose_name=u'Game Type')
	platform = models.CharField(max_length=10, choices=PLATFORM_CHOICES, default='None', verbose_name=u'Platform')
	description = models.TextField()
	min_players = models.IntegerField(verbose_name=u'Min. Players')
	max_players = models.IntegerField(verbose_name=u'Max. Players')
	playing_time = models.IntegerField(verbose_name=u'Playing Time (min)', blank=True, null=True)
	#bgg_id = models.IntegerField(blank=True, null=True, verbose_name=u'BoardGameGeek ID')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Game'
		verbose_name_plural = 'Games'

# A Physical Game copy
class GameCopy(models.Model):
	STATUS_CHOICES = (
		('Have', 'Available'),
		('Lent', 'Lent Out'),
		('Sold', 'Copy Sold'),
		('Lost', 'Copy Lost'))

	CONDITION_CHOICES = (
		('OK', 'OK'),
		('PC_Mss', 'Piece Missing'),
		('GM_Mss', 'Game Missing'))

	game = models.ForeignKey(Game)
	owner = models.ForeignKey(User)
	tracking_id = UUIDField()
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name=u'Copy Status', default='Have')
	condition = models.CharField(max_length=10, choices=CONDITION_CHOICES, verbose_name=u'Copy Condition', default='OK')
	description = models.TextField(verbose_name=u'Copy Description', blank=True, null=True)

	def __str__(self):
		return self.game.name + " owned by " + self.owner.username + " (Tracking ID " + self.tracking_id[:8].upper() + ")"
	def get_id(self):
		return self.tracking_id[:8].upper()

	class Meta:
		verbose_name = 'Game Copy'
		verbose_name_plural = 'Game Copies'

# A Game Like/Dislike
class GamePreference(models.Model):
	PREFERENCE_OPTIONS = (
		('Like', 'Like'),
		('Dislike', 'Dislike'))

	game = models.ForeignKey(Game)
	user = models.ForeignKey(User)
	preference = models.CharField(max_length=7, choices=PREFERENCE_OPTIONS, default='Like', verbose_name=u'Preference Type')

	def __str__(self):
		return self.user.username + " " + self.preference.lower() + "s " + self.game.name

	class Meta:
		verbose_name = 'Game Preference'
		verbose_name_plural = 'Game Preferences'