from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def dashboard(request):
    return render(request,'dashboard.html')
def login_user(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("login_page")
        else:
            return redirect('login_user')
    else:
        return render(request,'login.html')

def login_page(request):
    return render(request,'login_page.html')




def logout_view(request):
    logout(request)
    return redirect('login_user')

