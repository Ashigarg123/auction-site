from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import User, Mylist,MyComment,MyBid, Auction,Watchlist,Category

# Register your models here.

admin.site.register(User)
admin.site.register(Mylist)
admin.site.register(MyComment)
admin.site.register(MyBid)
admin.site.register(Auction)
admin.site.register(Watchlist)
admin.site.register(Category)
