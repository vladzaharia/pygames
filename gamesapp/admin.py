from django.contrib import admin
from gamesapp.models import Game, GameCopy, GamePreference

class OwnerInline(admin.TabularInline):
    model = GameCopy
    fields = ['game', 'owner']
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

class GameCopyAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic Information', {'fields': ['game', 'owner', 'tracking_id']}),
        ('Status Information', {'fields': ['status', 'condition', 'description']})
    ]
    list_display = ('game', 'owner', 'get_id')
    ordering = ['game']
    readonly_fields = ['tracking_id']

# Register Admin Information
admin.site.register(Game, GameAdmin)
admin.site.register(GameCopy, GameCopyAdmin)