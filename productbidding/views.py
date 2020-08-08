from django.shortcuts import render,redirect
from .models import Productdetails,Category,Orders,BidEntry,Bidwinner
import datetime



def Categoryshow(req,pk):
    cat=Category.objects.get(pk=pk)
    item=Productdetails.objects.filter(cat=cat)
    cat=Category.objects.all()
    return render(req,'category.html',{'item':item,'cat':cat})


def checkout(req):
    if not req.user.is_authenticated:
        return redirect('/accounts/login')
    return render(req,'checkout.html')

def home(req):
    product=Productdetails.objects.all()
    cat=Category.objects.all()
    return render(req,'home.html',{'product':product,'cat':cat})

def about(req):
    return render(req,'about.html')
def contact(req):
    return render(req,'contact.html')

def search(req):
    cat=Category.objects.all()
    try:
        query=req.GET['search']
        print(query)
    except:
        print("error")

    return render(req,'home.html',{'product':None,'cat':cat})

def bidduration(product):
    biden = str(product.bidet)
    hoursst, minst, secst = str(product.bidst).split(':')
    houren, minen, secen = biden.split(':')
    hoursrem = int(houren) - int(hoursst)
    duration = "0"
    if hoursrem >= 0:
        minrem = 0
        secrem = 0
        if int(minen) > int(minst):
            minrem = int(minen) - int(minst)
        elif int(minst) > int(minen) and hoursrem > 0:
            minrem = int(minst) - int(minen)
        if int(secst) > int(secen) and minrem > 0:
            secrem = int(secst) - int(secen)
        elif int(secen) > int(secst):
            secrem = int(secen) - int(secst)
        if hoursrem<10:
            hoursrem="0"+str(hoursrem)
        else:
            hoursrem=str(hoursrem)
        if minrem<10:
            minrem="0"+str(minrem)
        else:
            minrem=str(minrem)
        if secrem<10:
            secrem="0"+str(secrem)
        else:
            secrem=str(secrem)
        duration = hoursrem+":"+minrem+":"+secrem
    return duration

def bidamount(req,pk):
    if not req.user.is_authenticated:
        return redirect('/accounts/login')
    c = Category.objects.all()

    product=Productdetails.objects.get(pk=pk)
    biden=str(product.bidet)
    houren, minen, secen = biden.split(':')
    houren = int(houren)
    minen = int(minen)
    secen = int(secen)
    if datetime.datetime.now()>=datetime.datetime.now().replace(hour=houren,minute=minen,second=secen):
        return redirect('/home')
    if req.method=="POST":

        amount=req.POST['price']
        obj=BidEntry.objects.create(amount=amount,lname=req.user.last_name,fname=req.user.first_name,useremail=req.user.email,product_id=pk)
        obj.save()
        list=BidEntry.objects.filter(product_id=pk)
    return render(req, 'bidpage.html',{'duration':bidduration(product),'cat':c,'p':product,'list':list})

def bidwinners(req):
    if not req.user.is_authenticated:
        return redirect('/accounts/login')

    obj=BidEntry.objects.all()
    l=[]
    winnerlist=[]
    for i in obj:
        l.append(i.product_id)
    l=set(l)
    print(l)
    for i in l:

        bidl=BidEntry.objects.filter(product_id=i)
        max=bidl[0]
        w=max
        for j in bidl:
            if j.amount=="":
                continue

            if int(max.amount)<int(j.amount):
                max=j
                w=j
            if int(w.amount)==max:
                if w.bidtime>max.bidtime:
                    w=max
        if w is not None:

            winnerlist.append(w)
    for i in winnerlist:
        winl=Bidwinner.objects.all()
        entry=False
        for j in winl:
            if j.useremail==i.useremail:
                entry=True
        if entry is False:

            win=Bidwinner.objects.create(fname=i.fname,lname=i.lname,product_id=i.product_id,useremail=i.useremail,amount=i.amount,bidtime=i.bidtime)
            win.save()
    return render(req,'bidwinners.html',{'list':winnerlist})

def bid(req,pk):

    if not req.user.is_authenticated :
        return redirect('/accounts/login')
    c=Category.objects.all()
    product=Productdetails.objects.get(pk=pk)
    if product.bidstatus==True:
        biddate=product.biddate
        cyear, cmonth, cday = str(datetime.datetime.now())[:10].split('-')
        print(biddate)

        if biddate==datetime.date(int(cyear),int(cmonth),int(cday)):
            print("True")
            biden = str(product.bidet)
            hoursst, minst, secst = str(product.bidst).split(':')
            houren, minen, secen = biden.split(':')
            hoursst=int(hoursst)
            minst=int(minst)
            secst=int(secst)
            houren=int(houren)
            minen=int(minen)
            secen=int(secen)

            print("inside biddate")
            if datetime.datetime.now().replace(hour=houren,minute=minen,second=secen)<=datetime.datetime.now():
                print("last")
                product.bidstatus=False
                product.save()
            elif datetime.datetime.now()>=datetime.datetime.now().replace(hour=hoursst,minute=minst,second=secst) and datetime.datetime.now().replace(hour=houren,minute=minen,second=secen)>datetime.datetime.now().replace(hour=hoursst,minute=minst,second=secst)  :

                duration=bidduration(product)
                list=BidEntry.objects.filter(product_id=pk)
                print(duration)
                return render(req, 'bidpage.html', {'cat': c, 'p': product,'duration':duration,'list':list})

        else:


            if biddate<datetime.date(int(cyear),int(cmonth),int(cday)):


                product.bidstatus=False


                product.save()





    return render(req,'home.html',{'cat':c,"product":Productdetails.objects.all()})

def Order(req):
    if not req.user.is_authenticated:
        return redirect('/accounts/login')
    if req.method=="POST":
        name=req.POST['name']
        phone=req.POST['phone']
        amount=req.POST['amount']
        itemjson=req.POST['itemsJsons']
        add=req.POST['address']
        state=req.POST['state']
        email=req.POST['email']
        zip=req.POST['zip']
        city=req.POST['city']
        order=Orders(amount=amount,name=name,phone=phone,email=email,address=add,state=state,item_json=itemjson,zip_code=zip,city=city)
        order.save()
        check=True

        return render(req,'thank.html',{'check':check,'id':order.order_id})

