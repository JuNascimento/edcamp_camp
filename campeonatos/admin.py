from django.contrib import admin
from .models import Edicao
from .models import Campeonato


# Register your models here.

admin.site.register(Campeonato)
admin.site.register(Edicao)

