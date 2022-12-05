from datetime import date

from django.db import models
from django.db.models import CharField, DateField, IntegerField, FloatField, TextField
from django.forms import ModelChoiceField

from .settings import SEEDING_METHODS, TRAY_TYPES, GRIDS, HARVEST_UNITS, EVENTS, REASONS_FOR_TERMINATING

"""Market garden enterprise classes """

class Garden(models.Model):
    label = CharField(unique=True, max_length=20)
    number_of_beds = IntegerField()
    bed_length = FloatField()
    bed_width = FloatField()
    expected_number_of_rotations_per_year = FloatField()
    expected_income_per_rotation = FloatField()

class Crop(models.Model):
    name = CharField(max_length=20)
    seeding_method = CharField(choices=SEEDING_METHODS, max_length=20)
    number_of_seeds_per_hole = IntegerField()
    tray_type = IntegerField(choices=TRAY_TYPES)
    planting_grid = CharField(choices=GRIDS, max_length=20)
    direct_seeding_instructions = TextField()

class Variety(models.Model):
    name = CharField(max_length=20)
    crop = ModelChoiceField(queryset=Crop.objects.order_by('name'))

class Harvest(models.Model):
    date = DateField()
    variety = CharField(max_length=20)
    bed_number = CharField(max_length=20)
    quantity = FloatField()
    unit = CharField(choices=HARVEST_UNITS, max_length=20)

class Timeline(models.Model):
    date = DateField()
    event  = CharField(choices=EVENTS, max_length=20)
    bed_number = IntegerField()
    reason_for_termination = CharField(choices=REASONS_FOR_TERMINATING, max_length=20)
    notes = TextField()
