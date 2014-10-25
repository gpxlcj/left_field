#! -*- coding:utf-8 -*-
import httplib2, urllib2, os, re,urllib

def updata_test():
    connect = httplib2.Http()
    data = {
        'hint_id' : '121241242',
        'lover_id' : '125139212',
        'email_addr' : 'gpxlcj@gmail.com',
        'lover_name' : '富士',
        'hint_sex' : 0,

        }
    response,content = connect.request('http://0.0.0.0/newlover', 'POST', urllib.urlencode(data))
    write_file = open('xx.html','w')
    write_file.write(content)
    response,content = connect.request( 'http://0.0.0.0/updata','POST')
    print response

if __name__ == '__main__':
    updata_test()
