# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Vehicle, Profile, Accident


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        "license_plate",
        "brand",
        "type",
        "country",
        "insurance_name",
        "insurance_company",
        "has_damages",
    )
    search_fields = (
        "license_plate",
        "brand",
        "type",
        "insurance_name",
        "insurance_company",
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "phone_number",
        "email",
        "imsi",
        "imei",
        "driving_licence",
    )
    search_fields = (
        "first_name",
        "last_name",
        "phone_number",
        "email",
        "imsi",
        "imei",
        "driving_licence",
    )


@admin.register(Accident)
class AccidentAdmin(admin.ModelAdmin):
    list_display = (
        "vehicle_vA",
        "circumstance_vA",
        "damages_vA",
        "vehicle_vB",
        "circumstance_vB",
        "damages_vB",
    )
    list_filter = (
        "circumstance_vA",
        "circumstance_vB",
    )
