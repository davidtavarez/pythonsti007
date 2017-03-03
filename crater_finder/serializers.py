from rest_framework import serializers

from crater_finder.models import Vehicle, Employee, Crater, Fall


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()
    class Meta:
        model = Employee
        fields = ('id','name','phone_number','vehicle',)


class CraterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crater
        fields = '__all__'


class FallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fall
        fields = '__all__'
