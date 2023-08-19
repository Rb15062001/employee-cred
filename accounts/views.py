from django.shortcuts import render,redirect 
from django.contrib.auth.models import User,auth
from django.contrib  import messages
from django.http import HttpResponse

# Create your views here.



def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)  
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credintial')
            return redirect('login')
                   
    else:
         return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        
        # print(username)
        
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        print(username,email,password1,password2)
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'user name already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                 messages.info(request,'email id  already exits')
                 return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password1)
                print(user)
                user.save()
                return redirect('login')
        else:
          messages.info(request,'password doesnt match')  
          return redirect ('register')   
    else:
        return render(request,'register.html')     
    # return HttpResponse('hellow')
def logout(request):
      auth.logout(request)
      return redirect('/')
                
                
                    
                
                
        
        
        