from django.contrib import admin
from .models import Column, Card

# Register your models here.
admin.site.register(Card)

class Card(admin.TabularInline):
    model = Card

class ColumnAdmin(admin.ModelAdmin):
    inlines = [Card]

admin.site.register(Column, ColumnAdmin)