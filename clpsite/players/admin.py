from django.contrib import admin
from .models import Person, Country, Player, Rank, Setup, Agent, Rol, Setting, Map

admin.site.register(Person)
admin.site.register(Country)
#admin.site.register(Player)
admin.site.register(Rank)
admin.site.register(Setup)
admin.site.register(Setting)
admin.site.register(Agent)
admin.site.register(Rol)
admin.site.register(Map)

@admin.register(Player)
class Player(admin.ModelAdmin):
    list_display=('fullname','nick','rank')

    fieldsets =(
            ('Personal Data',{
                'fields':('fullname','birthday','country')
                }),
            ('Player Data',{
                'fields':('nick','played_hours','rank','setup','setting')
                }),
            )

