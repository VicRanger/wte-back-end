from django.contrib import admin
from .models import Canteen, Item, User, Comment

# Register your models here.


# class ItemInline(admin.TabularInline):
#     model = Item


# class CanteenInline(admin.TabularInline):
#     model = Canteen


# class UserInline(admin.TabularInline):
#     model = User


class CommentAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Main', {
            'fields': ('comment_text',),
        }],
        ['Time', {
            'fields': ('add_time', 'mod_time'),
        }],
        ['ForeignKey', {
            'fields': ('user', 'canteen', 'item'),
        }],
        ['ManyToMany', {
            'fields': ('up_users',),
        }],
    )
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Main', {
            'fields': ('openid','avatar_url','nickname','pk'),
        }],
    )

admin.site.register(Comment, CommentAdmin);
admin.site.register(User);
admin.site.register([Item, Canteen])
