from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator



class User(AbstractUser):
    pass

class Mylist(models.Model):
    pic=models.ImageField(upload_to = "images", null=True, blank=True)
    url= models.URLField(max_length=300, null=True)
    subject = models.CharField(max_length = 200)
    msg = models.TextField(null=True, blank=True)
    active= models.BooleanField(default=True)
    #cr_date = models.DateTimeField(auto_now_add=True)
    current_price = models.IntegerField(null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, default="vehicle", choices=(("Gadget", "Gadget"), ("Phone","Phone"), ("Cloth", "Cloth"), ("Furniture", "Furniture"), ("vehicle","vehicle")))
    #bid = models.IntegerField(default=0)
    uploaded_by = models.ForeignKey(to=User, on_delete=CASCADE,null=True, related_name="mylist" )
    bid = models.IntegerField(blank=True, null=True)
    bid_by = models.ForeignKey(to=User, on_delete=CASCADE,related_name="mylist2" ,default=1)
    #listing = models.ForeignKey(to=Mylist, on_delete=CASCADE,null=True)


    def __str__(self):
        return 'Posted on category- {} with title {}'.format(self.category, self.subject)

class MyComment(models.Model):
    listing = models.ForeignKey(to=Mylist, on_delete=CASCADE,)
    comment = models.TextField()
    #commented_by = models.ForeignKey(to=User, on_delete=CASCADE)
    #user = models.ForeignKey(User,on_delete=CASCADE)
    #cr_date = models.DateTimeField(auto_now_add=True)
    bid = models.IntegerField(blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    #pic=models.ImageField(upload_to = "images", null=True)

    def __str__(self):
        return 'Comment {} on {}'.format(self.comment, self.listing)

class MyBid(models.Model):
    #listing = models.ForeignKey(to=Mylist, on_delete=CASCADE)
    bid_by = models.ForeignKey(to=User, on_delete=CASCADE)
    #cr_date = models.DateTimeField(auto_now_add=True)
    current_price = models.IntegerField(null=True, blank=True)
    bid = models.IntegerField(blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "%s" % self.bid_by

class Auction(models.Model):
    listing = models.ForeignKey(Mylist, on_delete=models.CASCADE)
    number_of_bids = models.IntegerField()
    user = models.ForeignKey(User,on_delete=CASCADE)
    def __str__(self):
        return "%s" % self.number_of_bids

class Watchlist(models.Model):
    user = models.ForeignKey(User,on_delete=CASCADE,related_name="watchlist")
    listing = models.ForeignKey(Mylist, on_delete=models.CASCADE)


    def __str__(self):
        return 'Kept on watchlist {} by {}'.format(self.listing, self.user)

class Category(models.Model):

    category = models.CharField(max_length=20, default="vehicle", choices=(("Gadget", "Gadget"), ("Phome","Phone"), ("Cloth", "Cloth"), ("Furniture", "Furniture"), ("vehicle","vehicle")))
    #bid = models.IntegerField(default=0)
    listing = models.ForeignKey(Mylist, on_delete=models.CASCADE, related_name="+")
    #user = models.ForeignKey(User,on_delete=CASCADE, related_name="category")
    uploaded_by = models.ForeignKey(to=User, on_delete=CASCADE,null=True )

    def __str__(self):
        return 'Posted on category- {} by {}'.format(self.category, self.uploaded_by)
