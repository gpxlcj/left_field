#! -*-coding:utf-8-*-
from django.contrib import admin

from api.models import RenRenUser, LoverUser, ActivateCode, HintUser

admin.site.register(ActivateCode)
admin.site.register(RenRenUser)

