# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from cid.constants import CIRCUMSTANCE_CHOICES


class DateTimeModel(models.Model):
    creation_date = models.DateTimeField(verbose_name='Data creazione', auto_now_add=True, db_index=True)
    update_date = models.DateTimeField(verbose_name='Data ultima modifica', auto_now=True, db_index=True)

    class Meta(object):
        abstract = True


class Vehicle(DateTimeModel):
    license_plate = models.CharField(verbose_name='Targa', max_length=50, db_index=True, unique=True)
    brand = models.CharField(verbose_name='Marca', max_length=50, db_index=True, null=True, blank=True)
    type = models.CharField(verbose_name='Tipo', max_length=50, db_index=True, null=True, blank=True)
    country = models.CharField(
        verbose_name='Nazione immatricolazione',
        max_length=50,
        db_index=True,
        null=True,
        blank=True,
    )
    insurance_name = models.CharField(
        verbose_name='Denominazione polizza',
        max_length=50,
        db_index=True,
        null=True,
        blank=True,
    )
    insurance_company = models.CharField(verbose_name='Compagnia assicurativa', max_length=50, null=True, blank=True)
    insurance_start_date = models.DateTimeField(verbose_name='Polizza valida dal', null=True, blank=True)
    insurance_end_date = models.DateTimeField(verbose_name='Polizza valida fino al', null=True, blank=True)
    has_damages = models.BooleanField(
        verbose_name='Danni materiali', help_text="La polizza copre danni materiali?", default=False)

    class Meta:
        verbose_name = 'Veicolo'
        verbose_name_plural = 'Veicoli'
        ordering = ('-update_date', 'license_plate')

    def __str__(self):
        return "{} {} (TARGA: {})".format(self.type, self.brand, self.license_plate)


class Profile(DateTimeModel):
    first_name = models.CharField(verbose_name='Nome', max_length=50, db_index=True)
    last_name = models.CharField(verbose_name='Cognome', max_length=50, db_index=True)
    phone_number = models.CharField(verbose_name='Cellulare', max_length=50, null=True, blank=True, db_index=True)
    email = models.CharField(verbose_name='Email', max_length=50, null=True, blank=True, db_index=True)
    imsi = models.CharField(verbose_name='IMSI', max_length=50, null=True, blank=True, db_index=True)
    imei = models.CharField(verbose_name='IMEI', max_length=50, null=True, blank=True, db_index=True)
    driving_licence = models.CharField(verbose_name='Patente', max_length=50, null=True, blank=True, db_index=True)

    class Meta:
        verbose_name = 'Conducente'
        verbose_name_plural = 'Conducenti'
        ordering = ('first_name', 'last_name', '-update_date')

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Accident(DateTimeModel):
    vehicle_vA = models.ForeignKey(Vehicle, verbose_name='Veicolo A', related_name='accidents_vA')
    vehicle_vB = models.ForeignKey(Vehicle, verbose_name='Veicolo B', related_name='accidents_vB')
    circumstance_vA = models.IntegerField(
        verbose_name='Circostanze incidente A',
        default=1,
        choices=CIRCUMSTANCE_CHOICES,
        db_index=True,
    )
    circumstance_vB = models.IntegerField(
        verbose_name='Circostanze incidente B',
        default=1,
        choices=CIRCUMSTANCE_CHOICES,
        db_index=True,
    )
    damages_vA = models.CharField(verbose_name='Danni visibili A', max_length=250)
    damages_vB = models.CharField(verbose_name='Danni visibili B', max_length=250)
    observations_vA = models.CharField(verbose_name='Osservazioni A', max_length=250)
    observations_vB = models.CharField(verbose_name='Osservazioni B', max_length=250)

    class Meta:
        verbose_name = 'Sinistro'
        verbose_name_plural = 'Sinistri'
        ordering = ('-creation_date', )

    def __str__(self):
        return "Sinistro {} - {}".format(self.id, self.creation_date)
