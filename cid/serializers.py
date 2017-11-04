from rest_framework import serializers
from .models import Vehicle, Profile, Accident


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle
        fields = (
            'license_plate',
            'brand',
            'type',
            'country',
            'insurance_name',
            'insurance_company',
            'insurance_start_date',
            'insurance_end_date',
            'has_damages',
        )


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = (
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "imsi",
            "imei",
            "driving_licence",
        )


class AccidentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Accident
        fields = (
            "vehicle_vA",
            "circumstance_vA",
            "damages_vA",
            "vehicle_vB",
            "circumstance_vB",
            "damages_vB",
        )
