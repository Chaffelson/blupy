from django.contrib import admin

# Register your models here.

from .models import Adder


class AdderAdmin(admin.ModelAdmin):
    model = Adder

admin.site.register(Adder, AdderAdmin)
