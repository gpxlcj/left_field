# -*- coding:utf -8-*-
from django.db.models import *


class ActivateCode(Model):
    code = CharField(u'激活码', max_length = 20, unique = True)
    qq_id = CharField(u'qq号', max_length = 15, blank = True)

    def __unicode__(self):
        return "%s" %self.code

    class Meta:
        verbose_name = u'激活码'
        verbose_name_plural = u'激活码类'
class RenRenUser(Model):
    user_id = CharField(u'人人id', max_length = 30)
    name = CharField(u'姓名', max_length = 20, blank = True)
    loved_num = IntegerField(u'被多少人稀罕', default = 0)
    lover_id = CharField(u'爱者id', max_length = 30)
    have_love_id = TextField(u'喜欢过的人们的id', max_length = 1000)
    have_love_num = IntegerField(u'曾经稀罕过多少人', default = -1)
    match = BooleanField(u'配对情况', default = 0)

    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = u'用户类'
    def __unicode__(self):
        return "%s" %self.user_id 

class LoverUser(Model):
    user_id = CharField(u'人人id', max_length = 30)
    name = CharField(u'姓名', max_length = 20, blank = True)
    loved_num = IntegerField('u被多少人稀罕', default = 0)

    def __unicode__(self):
        return "%s" %self.user_id
    class Meta:
        verbose_name = u'高富白美帅'
        verbose_name_plural = u'高富白美帅类'

class HintUser(Model):
    
    user_id = CharField(u'人人id', max_length = 30)
    name = CharField(u'姓名', max_length = 20, blank = True)
    activate_code = ManyToManyField(ActivateCode, blank = True) 
    lover = ManyToManyField(LoverUser, blank = True)
    loved_num = IntegerField('被多少人稀罕', default = 0)
    match = BooleanField(u'配对是否成功',default = False)

    def __unicode__(self):
        return "%s" %self.user_id

    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = u'用户类'


