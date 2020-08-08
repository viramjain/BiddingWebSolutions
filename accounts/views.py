from django.shortcuts import render,redirect
from .models import SignUp
from django.contrib.auth.models import User,auth
# Create your views here.
def signup(req):
    if req.method=="POST":
        first_name=req.POST['first']

        last_name=req.POST['ln']

        contact_num=req.POST['num']

        city=req.POST['city']

        pincode=req.POST['pin_num']

        email=req.POST['email_id']

        password=req.POST['pwd']

        gender=req.POST['gender']

        address=req.POST['address']

        try:
            user=User.objects.create_user(email=email,last_name=last_name,first_name=first_name,password=password,username=email)

            SignUp.objects.create(user=user,contact_num=contact_num,pincode=pincode,city=city,gender=gender,address=address)
            auth.login(req,user)
            return redirect('/home')
        except:
            print("something went wrong")
    return render(req,'sign_up.html')
def forget(req):

    return render(req,'forget.html')
def login(req):
    if req.method == 'POST':
        u = req.POST['email']
        passw = req.POST['passw']
        user = auth.authenticate(username=u,password=passw)
        if user is not None:
            auth.login(req, user)
            return redirect('/home')

        else:
            print("something is wrong")


    return render(req,'login.html')
def logout(req):
    auth.logout(req)
    return redirect('/home')
