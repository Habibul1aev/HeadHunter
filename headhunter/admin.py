from django.contrib import admin

from headhunter.models import Category, Skills, Work, Schedules, Requirements, Country, City, Address, Resume


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    ordering = ('name',)

class SchedulesTable(admin.TabularInline):

    model = Schedules
    extra = 1


class RequirementsTable(admin.TabularInline):

    model = Requirements
    extra = 1

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'created_at')
    list_display_links = ('id', 'name')
    list_filter = ('id', 'from_price', 'to_price', 'is_publish')
    search_fields = ('category', 'user',)
    readonly_fields = ('created_at', 'updated_at')
    inlines = [SchedulesTable, RequirementsTable]
    ordering = ('created_at', )

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    ordering = ('name',)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'countries')
    list_display_links = ('id', 'countries')
    search_fields = ('id', 'countries')
    ordering = ('countries',)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'countries')
    list_display_links = ('id', 'city', 'countries')
    search_fields = ('id', 'city')
    ordering = ('city',)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'street', 'country_city')
    list_display_links = ('id', 'street', 'country_city')
    search_fields = ('id', 'street')
    ordering = ('country_city',)

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'profession', 'created_at')
    list_display_links = ('id', 'name')
    list_filter = ('id', 'profession', 'experience')
    search_fields = ('name', 'experience', 'profession')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('created_at', )