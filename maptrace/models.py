#! -*-coding:utf-8 -*-
from django.db import models
from django.db.models import *
from api.models import LoverUser, HintUser, RenRenUser
# Create your models here.

class Position(models.Model):
    
    name = CharField(u'地点名称', blank = True, max_length = 30)
    longitude = FloatField(u'纬度',default = 0)
    latitude = FloatField(u'经度',default = 0)
    time = CharField(u'时间',blank = True, max_length = 30)
    user = ManyToManyField(RenRenUser)
    
    

    class Meta:
        verbose_name = '位置'
        verbose_name_plural = '位置类'

    def __unicode__(self):
        return "%s" %self.id

