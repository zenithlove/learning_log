from django.urls import path
from . import views

app_name = 'users'
urlpatterns=[
    #path('login',login,{'template_name':r'users\login.html'},name='login'),
    path('register',views.register,name='register'),
    path('login',views.userlogin,name='login'),
    path('logout',views.userlogout,name='logout')
]



