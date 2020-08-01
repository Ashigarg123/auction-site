from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from django.views.generic.edit import ModelFormMixin
from .models import User, Mylist,MyComment, MyBid,Watchlist,Auction,Category
from .forms import MyCommentForm
from django.views.generic.base import TemplateView
from django.views.generic.list import MultipleObjectMixin
from django.db.models import Q
from django import forms


class MylistListView(ListView, FormMixin):
    model = Mylist



    def get_context_data(self, **kwargs):
        #Alllist = Mylist.objects.all()
        context ={}
        Alllist = Mylist.objects.filter(active=True)
        context["mylist_list"] = Alllist

        #context = super().get_context_data(**kwargs)

        #bid = MyBid.objects.filter(listing_id=self.kwargs.get('pk'))



        #context['bid'] =bid
        #context['form'] = MylistForm()

        if self.request.user.is_authenticated:
            Alllist = Mylist.objects.all()
            won=''
            msg=''
            for p1 in Alllist:
              p1.watched = False
              y = Watchlist.objects.filter(listing = p1, user=self.request.user)
              if y :
                  p1.watched = True
              y = Watchlist.objects.filter(listing = p1)

              if p1.uploaded_by == self.request.user:

                  can_close = True
                  #msg = "The listing is closed"

              else:
                  can_close = False
              if p1.active==False:
                msg="This listing is Closed!"

                if p1.bid_by_id==self.request.user.id:
                    won="Congrats!You won"
                else:
                    won=''





              else:
                  xyz= "This listing is currently Open!"







            #print(p1.active)
            #msg=''
            #won=""
            context["xyz"]=xyz
            context["can_close"]=can_close

            context["won"]=won
            context["msg"]=msg
            context["mylist_list"] = Alllist







        return context








    def post(self,request,*args,**kwargs):

        if request.method=="POST":
            bid=self.request.POST.get("bid")
            print(bid)
            listing_id= self.request.POST.get('id')
            bid_by_id=self.request.user.id
            print(bid_by_id)

            x=Mylist.objects.filter(id=listing_id).update(bid=bid,current_price=bid,bid_by_id=self.request.user.id)
            #print(x)

            #print(self.request.POST.get("x.id"))
            return HttpResponseRedirect(reverse("index"))






def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
@method_decorator(login_required, name="dispatch")
class create(CreateView):
    model = Mylist
    fields = ["pic", "url", "subject", "msg","category", "current_price",]
    def form_valid(self, form):
        self.object = form.save()
        self.object.uploaded_by = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

#class MylistListView(ListView):
    #model = Mylist









@method_decorator(login_required, name="dispatch")
class MylistDetailView(FormMixin,DetailView):
    model= Mylist
    #template_name = "auctions/mylist_detail.html"
    form_class = MyCommentForm
    #second_form_class = MylistForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = MyComment.objects.filter(listing_id=self.kwargs.get('pk'))
        user=self.request.user
        #commented_by = self.request.user









        #context['commented_by']=commented_by
        context['comments'] =comments
        #context["can_close"]=can_close

        #if 'form' not in context:
        context['form'] = MyCommentForm()
        context['user']=user

        return context

        #if 'form2' not in context:
            #context['form2'] = MylistForm()



        #return context

        #Alllist = Mylist.objects.all()
        #for p1 in Alllist:
            #p1.watched = False
            #for p1 in Alllist:
            #if y :
                #p1.watched = True
            #y = Watchlist.objects.filter(listing = p1)
        #listing = Auction.objects.all()
        #z = Mylist.objects.get(pk=self.kwargs.get('pk'))
        #listing2 = Auction.objects.filter(listing=Alllist, user=self.request.user)


        #context["mylist_list"] = Alllist

            #context['comments'] =comments

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        #if 'form' in request.POST:
        form_class = self.get_form_class()
        form_name = 'form'
        #else:
             #form_class = self.second_form_class
             #form_name = 'form2'
        form = self.get_form(form_class)




        if form.is_valid():
              #commented_by_id=self.kwargs.get('pk')
              #print(commented_by_id)
              #i=MyComment.objects.create(id=self.kwargs.get('pk'))
              #print(i)


              return self.form_valid(form)
            #self.object.commented_by_id= self.request.user


        else:
            return self.form_invalid(form)


    def form_valid(self, form):
        form.instance.listing = self.object



        #self.object.listing_id = s
        form.save()


        return super().form_valid(form)



def watch(req, pk):
    listing=Mylist.objects.get(pk=pk)

    Watching = Watchlist.objects.create(listing=listing,user=req.user)
    #Alllist = Mylist.objects.all()


    return HttpResponseRedirect(redirect_to="/")



def unwatch(req, pk):
    listing=Mylist.objects.get(pk=pk)
    Unwatched =Watchlist.objects.filter(listing=listing,user=req.user).delete()
    Alllist = Mylist.objects.all()


    return HttpResponseRedirect(redirect_to="/")

def Category2(request):

    return render(request, "auctions/category_list.html")



def vehicle(request):


    listing=Mylist.objects.filter(category="vehicle")
    #category = Category.objects.filter(listing__in=listing)
    print(listing)
    #print(category)
    context = {
    "category": listing
    }
    return render(request, "auctions/cat.html",context)

def phone(request):


    listing=Mylist.objects.filter(category="Phone")
    #category = Category.objects.filter(listing__in=listing)
    print(listing)
    #print(category)
    context = {
    "category": listing
    }
    return render(request, "auctions/cat.html",context)

def cloth(request):


    listing=Mylist.objects.filter(category="Cloth")
    #category = Category.objects.filter(listing__in=listing)
    print(listing)
    #print(category)
    context = {
    "category": listing
    }
    return render(request, "auctions/cat.html",context)

def gadget(request):


    listing=Mylist.objects.filter(category="Gadget")
    #category = Category.objects.filter(listing__in=listing)
    print(listing)
    #print(category)
    context = {
    "category": listing
    }
    return render(request, "auctions/cat.html",context)

def furniture(request):


    listing=Mylist.objects.filter(category="Furniture")
    #category = Category.objects.filter(listing__in=listing)
    print(listing)
    #print(category)
    context = {
    "category": listing
    }
    return render(request, "auctions/cat.html",context)
    #def get_context_data(self, *args,**kwargs):
        #context = super(CategoryListView, self).get_context_data(*args, **kwargs)
        #print(context)
        #return context
#def category_list_view(request):
    #category = Category.objects.filter()
    #context ={
    #"object_list": category
    #}
    #return render(request, "auctions/category_list.html",context)
def Watchli(request):

    listing=Watchlist.objects.filter(user=request.user)
    Alllist=Mylist.objects.filter(watchlist__in=listing)
    print(listing)
    print(Alllist)
    context = {
    "watchlist": Alllist
    }
    return render(request, "auctions/watchlist.html", context)

def close(request,pk):
    listing=Mylist.objects.get(pk=pk)
    Alllist=Mylist.objects.filter(id=pk).update(active=False)




    print(Alllist)
    return HttpResponseRedirect(redirect_to="/")



    #listing_id.update(active=False)
