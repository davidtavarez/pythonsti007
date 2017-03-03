from django.contrib import admin
from django.utils.safestring import mark_safe

from crater_finder.models import Crater, Employee, Vehicle, Fall


@admin.register(Crater)
class CraterAdmin(admin.ModelAdmin):
    list_display = (
        'nickname',
        'location',
        'discovered_at'
    )

    def location(self, instance):
        return mark_safe('<a href="https://www.google.com/maps/?q=%s,%s" target="_blank"><img src=http://maps.google.com/maps/api/staticmap?center=%s,%s&zoom=14&size=160x100&maptype=roadmap&sensor=false&language=&markers=color:red|label:none|%s,%s width="160" height="100"/></a>' % (
            str(instance.latitude), str(instance.longitude), str(instance.latitude),
            str(instance.longitude),
            str(instance.latitude), str(instance.longitude)))


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name',
        'phone_number',
    )

    list_filter = ('vehicle__model',)


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'manufacturer',
        'model',
        'year',
        'plate',
    )

    list_filter = ('manufacturer',)

    search_fields = ('plate',)


@admin.register(Fall)
class FallAdmin(admin.ModelAdmin):
    list_display = (
        'crater',
        'employee',
        'fallen_at',
    )

    list_filter = ('crater__nickname','employee__name',)
