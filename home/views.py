from django.shortcuts import render ,redirect , HttpResponse
from collections import OrderedDict
from django.db.models import Sum
from django.contrib.auth.models import User
from .models import ContactUs
from .models import Service
from .models import Haircut
from .models import CurrentOrder
from .models import Electrician
from .models import PestControl
from .models import HouseCleaning
from .models import Carpenter
from .models import Plumber
from .models import Painter
from .models import Salon
from django.contrib.auth  import authenticate,  login, logout
from .models import Profile
from django.contrib import messages

ok =False
login_credentials = False

def home(req):
    # print(req.method) POST
    allserv = Service.objects.all()
    user=req.user
    if(user.is_authenticated):
        norders=len(CurrentOrder.objects.filter(user=user))
    else:
        norders=0
    params = {'statuscontact' : "off" ,'services' : allserv ,'norders':norders}

    if(req.method == "POST"):
        try:
            # print(req.POST)
            # print(b[0].email) ;

            ContactUs.objects.create(
                name = req.POST.get('cname'),
                email = req.POST.get('cemail'),
                query = req.POST.get('ctext')
            )
            print("IT WORKED")
            params['statuscontact'] = "success"

        except:
            print("IT didnt WORKED!")
    params['ok'] = ok
    return render(req,"home.html" , params)



def card(req,myid):

    if(req.method == "POST"):

        # id = req.POST.get('sid')

        pref= Service.objects.get(id=myid).service_name
        chead = Service.objects.get(id = myid).card_heading
        # print(pref)
        service = {'Haircut': Haircut,'Salon':Salon,'Electrician':Electrician,'PestControl':PestControl,'HouseCleaning':HouseCleaning,
                   'Carpenter':Carpenter,'Plumber':Plumber,'Painter':Painter}
        pref=service[pref]
        alltype = pref.objects.all().order_by('type' , '-card_id' ,'price')

        types = pref.objects.all().values('type').distinct()
        # print(types)
        typeid = pref.objects.all().values('type_id').distinct()
        # print(typeid)

        stypes = {}
        for i in range(len(types)):
            stypes[types[i]['type']] = typeid[i]['type_id']
        # print(stypes)
        stypes = OrderedDict(sorted(stypes.items()))
        # print(stypes)
        user=req.user
        #len(CurrentOrder.objects.filter(user=user))
        if(user.is_authenticated):
            params = {'chead' : chead , 'types' : stypes , 'carddetails' : alltype , 'norders' : len(CurrentOrder.objects.filter(user=user))}
        # print(params)
        else:
            params = {'chead' : chead , 'types' : stypes , 'carddetails' : alltype , 'norders' : 0}
        return render(req, "cards.html" , params)

    else:
        return redirect("/")


def order(req):

    user=req.user
    if(user.is_authenticated):
        allorders = CurrentOrder.objects.filter(user=user)
        tprice = allorders.aggregate(Sum('price'))['price__sum']
        # print(len(allorders))
        params = {'allorders' : allorders , "no_of_orders" : len(allorders) , "tprice" :tprice }

        return render(req, "orders.html" , params)
    else:
        allserv = Service.objects.all()
        params = {'require_login': 'True', 'services': allserv}
        return render(req, 'home.html', params)

def updateorder(req):
    user = req.user
    if (req.method == 'POST' and user.is_authenticated):

        user = req.user
        service=req.POST.get('service')
        type = req.POST.get('type')
        price=int(req.POST.get('price'))

        orders = CurrentOrder(service=service,  type=type,price=price,user=user)
        orders.save()

    elif(req.method == 'POST' and not user.is_authenticated):
        allserv = Service.objects.all()
        params = {'require_login': 'True', 'services': allserv}
        return render(req, 'home.html', params)

    else:
        return redirect('/')

    return redirect('/order')

def deleterow(req):

    id = req.GET.get('orderid')
    try:
        CurrentOrder.objects.filter(id=id).delete()

    except Exception as e:
        print(e)
        print("IT Didnt worked")

    return redirect('/')

def handleSignup(request):
    ok= False
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneous input

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        phone=request.POST['phone']
        address=request.POST['address']
        city=request.POST['city']
        state=request.POST['state']
        pincode=request.POST['pin']
        profile = Profile(user=myuser, address=address, city=city, state=state,pincode=pincode,phone=phone)
        profile.save()

        ok=True
        allserv = Service.objects.all()
        params = {'ok': ok, 'services': allserv}
        return render(request,'home.html',params)

    else:
        return HttpResponse('404 -Error')

def signup(request):
    return render(request,'signup.html')

def Login(request):
    if(request.user.is_authenticated):
        allserv = Service.objects.all()
        params = {'nice': 'True', 'services': allserv}
        return render(request, 'home.html', params)
    return render(request,'login.html')

def handleLogin(request):

    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            login_credentials = True
            allserv = Service.objects.all()
            params = {'login_credentials': login_credentials, 'services': allserv}
            print(user)

            return render(request, 'home.html', params)
        else:
            login_credentials = False
            allserv = Service.objects.all()
            params = {'login_credentials': login_credentials, 'services': allserv}
            return render(request, 'home.html', params)

    return HttpResponse("404- Not found")

def handelLogout(request):
    if request.user.is_authenticated:
        logout(request)
        allserv = Service.objects.all()
        params = {'logouts': 'True', 'services': allserv}
        return render(request, 'home.html', params)
    else:
        return redirect('/')

def bookOrder(request):
    if(request.user.is_authenticated):
        user_details=Profile.objects.get(user=request.user)
        user=request.user
        allorders = CurrentOrder.objects.filter(user=user)
        tprice = allorders.aggregate(Sum('price'))['price__sum']
        params={'name':user.first_name+" "+ user.last_name,'phone':user_details.phone,'email':user.email,'pincode':user_details.pincode,
                  'city':user_details.city,'state':user_details.state,'address':user_details.address,'number':len(allorders),
                'tprice':tprice}
        print(params)
        return render(request,'bookOrder.html',params)

    else:
        return redirect('/')


