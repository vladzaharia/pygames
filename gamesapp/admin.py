from django.contrib import admin
from gamesapp.models import Game, GameCopy, GamePreference

class OwnerInline(admin.TabularInline):
    model = GameCopy
    extra = 1

class PreferenceInLine(admin.TabularInline):
    model = GamePreference
    extra = 1

class GameAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Game Information',    {'fields': ['name', ('game_type', 'platform'), 'description']}),
        ('Playing Information', {'fields': [('min_players', 'max_players'), 'playing_time']}),
    ]
    inlines = [OwnerInline, PreferenceInLine]
    list_display = ('name', 'game_type', 'platform')
    list_filter = ['game_type', 'platform']
    search_fields = ['name']
    ordering = ['name']

# Register Admin Information
admin.site.register(Game, GameAdmin)
#admin.site.register(OwnedGame)