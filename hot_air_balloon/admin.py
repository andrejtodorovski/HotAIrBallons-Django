from django.contrib import admin

# Register your models here.
from .models import Pilot, Balloon, Airline, AirlinePilot, Flight


class PilotAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')
    list_filter = ('role', 'year_of_birth')
    search_fields = ('name', 'surname')


class BalloonAdmin(admin.ModelAdmin):
    list_display = ('max_passengers', 'type', 'manufacturer')
    list_filter = ('type', 'manufacturer')
    search_fields = ('manufacturer', 'type')
    sortable_by = ('max_passengers',)


# inline
class AirlinePilotAdmin(admin.TabularInline):
    model = AirlinePilot
    extra = 0


class AirlineAdmin(admin.ModelAdmin):
    inlines = [AirlinePilotAdmin]
    list_display = ('name',)
    list_filter = ('year_founded', 'coverage_EU')
    search_fields = ('name', 'coverage_EU')


class FlightAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_filter = ('airline', 'pilot', 'balloon', 'user')
    search_fields = ('airline', 'pilot', 'balloon', 'user')
    list_display = ('code', 'airline', 'pilot', 'balloon', 'user')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Pilot, PilotAdmin)
admin.site.register(Balloon, BalloonAdmin)
admin.site.register(Airline, AirlineAdmin)
admin.site.register(Flight, FlightAdmin)
