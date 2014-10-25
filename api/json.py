#! -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import simplejson

def render_json(_dict):
    json = simplejson.dumps(_dict, ensure_ascii = False)
    mimetype = 'application/json'
    return HttpResponse(json, mimetype = mimetype)
