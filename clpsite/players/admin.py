from django.contrib import admin
from .models import Person, Country, Player, Rank

admin.site.register(Person)
admin.site.register(Country)
#admin.site.register(Player)
admin.site.register(Rank)

@admin.register(Player)
class Player(admin.ModelAdmin):
    list_display=('fullname','nick','rank')

    fieldsets =(
            ('Personal Data',{
                'fields':('fullname','birthday','country')
                }),
            ('Player Data',{
                'fields':('nick','played_hours','rank')
                }),
            )

