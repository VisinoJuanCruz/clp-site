from django.contrib import admin
from .models import Person, Country, Player, Rank, Agent, Rol, Map,Tier

admin.site.register(Person)
admin.site.register(Country)
#admin.site.register(Player)
admin.site.register(Rank)
admin.site.register(Agent)
admin.site.register(Rol)
admin.site.register(Map)
admin.site.register(Tier)

@admin.register(Player)
class Player(admin.ModelAdmin):
    list_display=('fullname','nick','rank')

    fieldsets =(
            ('Personal Data',{
                'fields':('fullname','birthday','country','description','image')
                }),
            ('Player Data',{
                'fields':('nick','played_hours','rank','agents')
                }),
            ('Setting Data',{
                'fields':('sensivility','dpi')
                }),
            ('Setup Data',{
                'fields':('monitor','keyboard','mouse','mousepad','headset')
                }),
            )

