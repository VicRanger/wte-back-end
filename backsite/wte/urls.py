from django.urls import path;

from . import views;

app_name = 'wte';

urlpatterns = [
    path('openid/',views.openid,name="openid"),
    path('canteen_list/',views.canteen_list,name="canteen-list"),
    path('canteen/',views.canteen,name="canteen"),
    path('comment_list/',views.comment_list,name="comment-list"),
    path('comment/',views.comment,name="comment"),
    path('comment_up/',views.comment_up,name="comment_up"),
    path('user/',views.user,name="user"),
    path('init/',views.init,name="init"),
    path('checkok/',views.checkok,name='checkok'),
];