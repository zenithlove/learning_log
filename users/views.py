from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail


# Create your views here.
def register(request):
    if request.method != 'POST':
        return render(request,r'users\register.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        print(username,password,email,type(email))
        print([email])
        print(['281389404@qq.com'])
        #try:
        if email is not None:
            #try:
            print("---------before send_main-----------")
            #send_mail('register learning logs','thank you for registering vvvvvv','',list(email),fail_silently=False,)  
            send_mail('register learning logs','thank you for registering vvvvvv','',[email])
            #except:
            #return HttpResponse('Error.')              
        #     except smtplib.SMTPException:
        #         return HttpResponse('SMTPException.')
        #     except smtplib.SMTPResponseException:
        #         return HttpResponse('SMTPResponseException')
        #     except smtplib.SMTPSenderRefused:
        #         return HttpResponse('SMTPSenderRefused.')
        #     except smtplib.SMTPRecipientsRefused:
        #         return HttpResponse('SMTPRecipientsRefused.')
        #     except smtplib.SMTPDataError:
        #         return HttpResponse('SMTPDataError.')
        #     except smtplib.SMTPConnectError:
        #         return HttpResponse('SMTPConnectError.')
        #     except smtplib.SMTPHeloError:
        #         return HttpResponse('SMTPHeloError.')
        #     except smtplib.SMTPNotSupportedError:
        #         return HttpResponse('SMTPNotSupportedError.')
        #     else smtplib.SMTPAuthenticationError:
        #         return HttpResponse('SMTPAuthenticationError.')
        print("------------before create_user------------------")
        authenticated_user = User.objects.create_user(username,email,password)
        if authenticated_user is not None:
            print("----------------register------------------")

            login(request,authenticated_user)
            print("-------******log succeed*************-------------")
            return HttpResponseRedirect(reverse('learning_logs:index'))
        #except :
            #print("--------register info is wrong---------------")
            #context = {'error_msg':'something is wrong'}
            #return render(request,r'users\register.html',context)

    

def userlogin(request):
    context = {}
    if  request.method != 'POST':
        print("********************user**********************************")

    else:

        username = request.POST['username']
        password = request.POST['password']
        print(request.POST['username'],request.POST['password'])
    
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("********************user is authenticated**********************************")
            login(request, user)
            # Redirect to a success page.
            context = {'user':user}
            return render(request,r'learning_logs\index.html',context)
            
        else:
            # Return an 'invalid login' error message.
            context = {'error_msg':"username or password is not right"}

    return render(request,r'users\login.html',context)

def userlogout(request):
    print('------in logout--------')
    logout(request)   
    return  HttpResponseRedirect(reverse('users:login'))