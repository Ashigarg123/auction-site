from django import forms
from .models import MyComment,Mylist,MyBid
from django.contrib.auth.models import User


class MyCommentForm(forms.ModelForm):
    class Meta:
        model = MyComment
        fields = { 'comment'}
