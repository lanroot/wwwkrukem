import datetime
from django.db import models

# Create your models here.
class Person(models.Model):
    pers_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    gtel = models.CharField(max_length=32, blank=True)
    mtel = models.CharField(max_length=32, blank=True)
    stel = models.CharField(max_length=32, blank=True)
    fax = models.CharField(max_length=32, blank=True)
    email = models.EmailField()
    post = models.CharField(max_length=255, blank=True)
    office = models.CharField(max_length=255, blank=True)
    subdiv = models.CharField(max_length=255, blank=True)
    visible = models.SmallIntegerField()
    active = models.SmallIntegerField()
    div_id = models.IntegerField()
    last_update = models.DateTimeField(default=datetime.datetime.now, auto_now_add=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/userdir/get/%i" % self.pers_id

    class Meta:
        db_table = u'persons'
        ordering = ['name']

class City(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    ccode = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = u'cities'
        ordering = ['id']

class Div(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=32)
    mcode = models.CharField(max_length=8)
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=128)
    city_id = models.IntegerField()
    pri = models.SmallIntegerField()
    addr_pref = models.CharField(max_length=9)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = u'divs'
