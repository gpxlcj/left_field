#! -*-coding:utf-8-*-
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.utils import simplejson
from api.json import render_json
from api.models import RenRenUser, HintUser, LoverUser
from api.email import send_invite_mail

ERROR_STATUS = {'status':0}
SUCCESS_STATUS = {'status':1}

def new_lover(request):
 
    if request.method == 'POST':
        try:
            user_id = request.POST.get('hint_id')
            lover_id = request.POST.get('lover_id')
            if request.POST.get('email_addr'):
                email = request.POST.get('email_addr')
                name = request.POST.get('lover_name')
                send_invite_mail(email, name)
            else:
                pass
            if RenRenUser.objects.filter(user_id = user_id):
                renren_user = RenRenUser.objects.get(user_id = user_id)
            else:
                renren_user = RenRenUser(user_id = user_id)
            if renren_user.lover_id:
#                have_love_user = RenRenUser.objects.get(user_id = renren_user.lover_id)
#                have_love_user.save()
#                if renren_user.lover_id == lover_id:
#                    have_love_user.loved_num += 1
#                    have_love_user.save()
#                    return render_json(SUCCESS_STATUS)
#                if renren_user.have_love_id:
#                    for i in renren_user.have_love_id.split(','):
#                        if i == renren_user.lover_id:
#                            renren_user.have_love_num -= 1
#                            break
#                    else:
#                        renren_user.have_love_id += ','
#                        renren_user.have_love_id += renren_user.lover_id
#                else:
                renren_user.have_love_id += ','
                renren_user.have_love_id += renren_user.lover_id
            else:
                pass
            renren_user.have_love_num += 1
            renren_user.lover_id = lover_id
            renren_user.save()
#喜欢的人的数据变化
            if RenRenUser.objects.filter(user_id = lover_id):
                lover_user = RenRenUser.objects.get(user_id = lover_id, loved_num = 0)
            else:
                lover_user = RenRenUser(user_id = lover_id)
            lover_user.loved_num += 1
            if lover_user.lover_id == user_id:
                renren_user.match = 1
                lover_user.match = 1


            lover_user.save()
            renren_user.save()
            data = {
                'hint_loved_num':renren_user.loved_num,
                'lover_loved_num':lover_user.loved_num,
                'match':renren_user.match,
                'hint_have_love_num':renren_user.have_love_num,
                }
            return render_json(data)
        except:
            return render_json(ERROR_STATUS)
    else:
        return render_json(ERROR_STATUS)
            
def updata(request):
    
    if request.method == 'POST':
        user_id = request.POST.get('hint_id')
        try:
            if RenRenUser.objects.filter(user_id = user_id):
                renren_user = RenRenUser.objects.get(user_id = user_id)
            else:
                renren_user = RenRenUser(user_id = user_id)
            renren_user.save()
            temp = 0
            if renren_user.have_love_num<0:
                temp = 1
            #renren_user_list = renren_user.have_love_id.split() 
            data = {
                'hint_loved_num':renren_user.loved_num,
                'match':renren_user.match,
                'hint_have_love_num':renren_user.have_love_num+temp,
                }
            return render_json(data)
        except:
            return render_json(ERROR_STATUS)
    else:
        return render_json(ERROR_STATUS)


def have_love(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        try:
            if RenRenUser.objects.filter(user_id = user_id):
                renren_user = RenRenUser.objects.get(user_id = user_id)
            else:
                return render_json(ERROR_STATUS)
            if renren_user.have_love_id:
                have_love_id_list = renren_user.have_love_id.split(',')
                have_love_id_list.append(renren_user.lover_id)
            else:
                have_love_id_list = list()
                have_love_id_list.append(renren_user.lover_id)
            data = {
                'have_love_id_list':have_love_id_list,
                }
            return render_json(data)
        except:
            return render_json(ERROR_STATUS)
    else:
        return render_json(ERROR_STATUS)
