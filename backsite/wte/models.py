from django.db import models;
from django.utils import timezone;
import datetime;
# Create your models here.

class Canteen(models.Model):
    name = models.CharField(max_length=200);
    ename = models.CharField(max_length=200);
    intro = models.CharField(max_length=500,default='暂无简介');
    pos = models.CharField(max_length=200,default='北京邮电大学沙河校区');
    def __str__(self):
        return self.name;

class Item(models.Model):
    name = models.CharField(max_length=200);
    ename = models.CharField(max_length=200);
    intro = models.CharField(max_length=500);
    def __str__(self):
        return self.name;

class User(models.Model):
    openid = models.CharField(max_length=200);
    avatar_url = models.CharField(max_length=200);
    code = models.CharField(max_length=200);
    language = models.CharField(max_length=100,default="null");
    city = models.CharField(max_length=100,default="null");
    province = models.CharField(max_length=100,default="null");
    country = models.CharField(max_length=100,default="null");
    gender = models.CharField(max_length=10,default="null");
    add_time = models.DateTimeField(verbose_name='create-time',default=timezone.now);
    nickname = models.CharField(max_length=200);
    def __str__(self):
        return 'pk:'+str(self.pk) + ' - nickname:' + self.nickname + ' (' + self.gender+')';

class Comment(models.Model):
    up_users = models.ManyToManyField(User,related_name='up_comment',blank=True);
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True);
    canteen = models.ForeignKey(Canteen,on_delete=models.SET_NULL,blank=True,null=True);
    item = models.ForeignKey(Item,on_delete=models.SET_NULL,blank=True,null=True);
    comment_text = models.CharField(max_length=200);
    add_time = models.DateTimeField(verbose_name='create-time',default=timezone.now);
    mod_time = models.DateTimeField(verbose_name='last-mod-time',default=timezone.now);
    canteen_ename = models.CharField(max_length=200,default='none');
    item_ename = models.CharField(max_length=200,default='none');
    user_openid = models.CharField(max_length=200,default='none');

    def __str__(self):
        return self.comment_text + " （作者：" + self.user.nickname + ")";
    def get_dict(self):
        ret = {};
        ret['pk'] = self.pk;
        ret['comment_text'] = self.comment_text;
        ret['up_count'] = self.up_users.count();
        ret['user_nickname'] = self.user.nickname;
        ret['user_avatar_url'] = self.user.avatar_url;
        ret['add_time'] = self.add_time.strftime("%Y-%m-%d %H-%M-%S");
        print(ret);
        return ret;

