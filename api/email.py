#! -*- coding:utf-8 -*-
from django.core.mail import send_mail

def send_invite_mail(emailurl, name):
    try:
        title = name+u'你好，有个人偷偷喜欢你呦'
        content = u"有人在APP《你想多了》中向你表达爱意呦，点击下列链接www.ziqiang.net"
        send_mail(title, content,'gpxlcj@126.com',[emailurl])
        return True
    except:
        return False
