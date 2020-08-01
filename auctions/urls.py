from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.MylistListView.as_view(success_url="/"), name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("add", views.create.as_view(success_url="/"), name="create"),
    #path('mylist/', views.MylistListView.as_view(), name="list"),
    path('mylist/<int:pk>', views.MylistDetailView.as_view(success_url="/"), name="p1"),
    path('watchlist/add/<int:pk>', views.watch, name="watch"),
    path('watchlist/remove/<int:pk>', views.unwatch, name="unwatch"),
    path('category/', views.Category2, name="category"),
    path('vehicle/', views.vehicle, name="vehicle"),
    path('gadget/', views.gadget, name="gadget"),
    path('cloth/', views.cloth, name="cloth"),
    path('phone/', views.phone, name="phone"),
    path('furniture/', views.furniture, name="furniture"),
    path('mylist/close/<int:pk>', views.close, name="p2"),



    path('mywatchlist/', views.Watchli, name="watchlist"),


]
