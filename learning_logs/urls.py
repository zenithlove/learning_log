#from django.contrib import admin

#method 1
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('topics/',views.showtopics,name='showtopics'),
    path('topics/<int:topicindex>',views.showentry,name='showentry'),
    path('new_topic/',views.new_topic,name='new_topic'),
    path('new_entry/<int:topic_id>',views.new_entry,name='new_entry'),
] 
app_name = "learning_logs"


'''
#METHOND 2
from django.urls import path

import sys
import os

sys.path.append(os.path.dirname(__file__))
print(os.path.dirname(__file__))
print(sys.path)
import  views
urlpatterns = [
    path('',views.index,name='index'),
    path('topics/',views.showtopics,name='showtopics'),
    path('topics/<int:topicindex>',views.showentry,name='showentry'),
    path('new_topic/',views.new_topic,name='new_topic'),
] 
app_name = "learning_logs"
'''