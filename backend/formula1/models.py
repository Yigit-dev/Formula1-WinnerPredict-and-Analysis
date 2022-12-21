from django.db import models

class Formula1(models.Model):
    formula1 = models.JSONField()

class Teams(models.Model):
    teams = models.JSONField()

class Races(models.Model):
    races = models.JSONField()

class Drivers(models.Model):
    drivers = models.JSONField()