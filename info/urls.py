from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    
    #path('', views.home,name="home"),
    path('',views.Insertrecord, name ="insert"),
    path('record',views.recordpage,name='recordpage'),
  #  path('check',views.getdata,name='getdata'),

]
