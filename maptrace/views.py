#! -*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from django.Http import HttpResponse
from django.utils import *
from api.models import RenRenUser
ERROR_STATUS = {'status':0}
SUCCESS_STATUS = {'status':1}

def lover_position(request):
    
    if request.method == 'POST':
        try:
            longitude  = request.POST.get('longitude')
            latitude = request.POST.get('latitude')
            user_id = request.POST.get('user_id')
            renren_user = RenRenUser(user_id = user_id)
            position = Position(latitude = latitude, longitude = longitude, user = renren_user)
            return render_json(SUCCESS_STATUS)
        except:
            return render_json(ERROR_STATUS)
            

        
