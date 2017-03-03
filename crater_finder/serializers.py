from rest_framework import serializers

from crater_finder.models import Vehicle, Employee, Crater, Fall


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()

    class Meta:
        model = Employee
        fields = ('name', 'phone_number', 'vehicle',)


class CraterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Crater
        fields = '__all__'


class CraterListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='crater-detail', format='html')
    class Meta:
        model = Crater
        fields = ('nickname', 'url')


class FallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fall
        fields = '__all__'
        depth = 5
