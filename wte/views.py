# -*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt 
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .mylib import Http
from .models import Canteen, Item, User, Comment;
from django.core import serializers
import json;
# Create your views here.
# b09a9f8726bf1b3b115ff0bd223dfcc6
# wx099d180959c58707
appID = 'wx099d180959c58707'
secret = 'b09a9f8726bf1b3b115ff0bd223dfcc6'


def openid(request):
    if(request.method == 'GET'):
        query_data = request.GET.dict()
        code = query_data['code']
        data = Http.Get("https://api.weixin.qq.com/sns/jscode2session?", {
            'grant_type': 'authorization_code',
            'appid': appID,
            'secret': secret,
            'js_code': code
        })
        return HttpResponse(data, content_type="application/json")

    # POST : create the user with user's openid, avator_url and nickname
    # GET : check if user exists in the database, if return T or F

def user(req):
    if req.method == 'POST':
        query_data = req.POST.dict();
        user_obj = User(openid=query_data['openid'],avatar_url=query_data['avatar_url'],nickname=query_data['avatar_url']);
        user_obj.save();
    if req.method == 'GET':  # POST
        query_data = req.GET.dict();
        user_query = User.objects.filter(openid=query_data['openid']);
        if user_query.count() > 0:
            return JsonResponse({'data': 1});
        else:
            return JsonResponse({'data': 0});
        pass;
    return HttpResponse({'data': 'None'}, content_type="application/json")

@csrf_exempt 

    # GET : get the comment with query condition
    # POST : create a comment with user, canteen and item.

def comment(req):
    if(req.method == 'GET'):
        pass;
    if(req.method == 'POST'):  # POST
        ret_dict = {};
        query_data = json.loads(req.body);
        print(query_data);
        user_query = User.objects.filter(openid=query_data['user_openid']);
        if user_query.count() <= 0:
            return JsonResponse({'error': '用户不存在'});
        user = user_query[0];
        ret_dict['user'] = user.__str__();
        obj = Comment(user=user, comment_text=query_data['comment_text']);
        obj.user_openid = user.openid;
        obj.save();
        if 'canteen_ename' in query_data:
            canteen_query = Canteen.objects.filter(
                ename=query_data['canteen_ename']);
            if canteen_query.count() > 0:
                canteen = canteen_query[0];
                obj.canteen = canteen;
                obj.canteen_ename = canteen.ename;
                ret_dict['canteen'] = canteen.ename;
                obj.save();
        if 'item_ename' in query_data:
            item_query = Item.objects.filter(ename=query_data['item_ename']);
            if item_query.count() > 0:
                item = item_query[0];
                print(item);
                obj.item = item;
                obj.item = item_ename;
                ret_dict['item'] = item.__str__();
                obj.save();
        return JsonResponse({'query': query_data, 'data': ret_dict}, content_type="application/json");
    return JsonResponse({'data': 'None'})


def comment_up(req):
    if req.method == 'POST':
        pass;
    if req.method == 'GET':
        ret_str = [];
        query_data = req.GET.dict();
        print('comment POST :%s' % (query_data));


def comment_list(req):
    if(req.method == 'GET'):
        query_data = req.GET.dict();
        print('comment_list got %s' % (query_data));
        comment_query = Comment.objects.all();
        if 'user_openid' in query_data:
            comment_query = comment_query.filter(
                user__openid=query_data['user_openid']);
        if 'canteen_ename' in query_data:
            comment_query = comment_query.filter(
                canteen__ename=query_data['canteen_ename']);
        if 'item_ename' in query_data:
            comment_query = comment_query.filter(
                item__ename=query_data['item_ename']);
        ret = {};
        ret['data'] = comments_to_list(comment_query);
        return JsonResponse(ret);
    return JsonResponse({}, content_type="application/json")


def canteen(req):
    if req.method == 'GET':
        query_data = req.GET.dict();
        canteen_query = Canteen.objects.filter(ename=query_data['ename']);
        pass;
    if req.method == 'POST':
        pass;

    return HttpResponse({}, content_type="application/json");


def canteen_list(req):
    return HttpResponse({}, content_type="application/json")


def comments_to_list(data):
    if data.count() <= 0:
        return [];
    cmt_list = list(data);
    ret = [item.get_dict() for item in cmt_list];
    return ret;


def canteen(req):
    if req.method == 'GET':
        pass;
    if req.method == 'POST':
        query_data = req.GET.dict();
        print('canteen GET :%s' % (query_data));
        obj = Canteen(name=query_data['name'], ename=query_data['ename']);
        obj.save();
    return JsonResponse({}, content_type="application/json");


def init(req):
    ret_str = [];
    canteen_data = [
        dict(name='南一', ename='s1'),
        dict(name='南二', ename='s2'),
        dict(name='南三', ename='s3'),
        dict(name='南四', ename='s4'),
        dict(name='南五', ename='s5'),
        dict(name='北一', ename='n1'),
        dict(name='北二', ename='n2'),
        dict(name='北三', ename='n3'),
        dict(name='北四', ename='n4'),
        dict(name='北五', ename='n5'),
    ];
    for item in canteen_data:
        results=Canteen.objects.filter(ename = item['ename']);
        if results.count():
            continue;
        Canteen.objects.create(name = item['name'], ename = item['ename']);
        print('create' + str(item));
        ret_str += str(item)+'<br />';
    return HttpResponse(ret_str);

def checkok(req):
    return HttpResponse('OK');