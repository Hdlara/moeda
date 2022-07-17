from django.contrib import admin

# Register your models here.
from .models import CandleStick


class CandleStickAdmin(admin.ModelAdmin):
    model = CandleStick
    list_display = ('dolar', 'euro', 'jpy', 'real', 'period')

admin.site.register(CandleStick, CandleStickAdmin)