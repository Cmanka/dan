from django.contrib import admin
from .models import *


class QualificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'experience')
    list_display_links = ('id', 'name', 'description', 'experience')


class TitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'premium')
    list_display_links = ('id', 'name', 'description', 'premium')


class CupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'premium')
    list_display_links = ('id', 'name', 'description', 'premium')


class AchievementAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cup', 'title', 'match_count')
    list_display_links = ('id', 'name', 'cup', 'title', 'match_count')


class PlayerCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name', 'description')


class PersonnelCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name', 'description')


class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'salary', 'start','term')
    list_display_links = ('id', 'name', 'salary', 'start','term')


class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'first_name', 'last_name', 'middle_name', 'country', 'age', 'phone', 'contract', 'position',
        'achievement',
        'qualification')
    list_display_links = (
        'id', 'first_name', 'last_name', 'middle_name', 'country', 'age', 'phone', 'contract', 'position',
        'achievement',
        'qualification')


class PersonnelAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'first_name', 'last_name', 'middle_name', 'email', 'phone', 'contract', 'position', 'qualification')
    list_display_links = (
        'id', 'first_name', 'last_name', 'middle_name', 'email', 'phone', 'contract', 'position', 'qualification')


admin.site.register(Qualification, QualificationAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Cup, CupAdmin)
admin.site.register(Achievement, AchievementAdmin)
admin.site.register(PlayerCategory, PlayerCategoryAdmin)
admin.site.register(PersonnelCategory, PersonnelCategoryAdmin)
admin.site.register(Personnel, PersonnelAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Contract, ContractAdmin)
