from django.shortcuts import render ,redirect
from collections import OrderedDict
from django.db.models import Sum
from .models import ContactUs
from .models import Service
from .models import Haircut
from .models import CurrentOrder


def home(req):
    # print(req.method) POST
    allserv = Service.objects.all()
    params = {'statuscontact' : "off" ,'services' : allserv}

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

    return render(req,"home.html" , params)



def card(req):

    if(req.method == "POST"):

        id = req.POST.get('sid')

        chead = Service.objects.get(id = id).card_heading

        service = {3 : Haircut}
        alltype = service[int(id)].objects.all().order_by('type' , '-card_id' ,'price')

        types = service[int(id)].objects.all().values('type').distinct()
        typeid = service[int(id)].objects.all().values('type_id').distinct()

        stypes = {}
        for i in range(len(types)):
            stypes[types[i]['type']] = typeid[i]['type_id']

        stypes = OrderedDict(sorted(stypes.items()))

        len(CurrentOrder.objects.all())
        params = {'chead' : chead , 'types' : stypes , 'carddetails' : alltype , 'norders' : len(CurrentOrder.objects.all())}
        # print(params)
        return render(req, "cards.html" , params)

    else:
        return redirect("/")


def order(req):

    allorders = CurrentOrder.objects.all()
    tprice = CurrentOrder.objects.aggregate(Sum('price'))['price__sum']
    # print(len(allorders))
    params = {'allorders' : allorders , "no_of_orders" : len(allorders) , "tprice" :tprice }

    return render(req, "orders.html" , params)


def updateorder(req):

    if (req.method == 'POST'):

        CurrentOrder.objects.create(
            service=req.POST.get('service'),
            type=req.POST.get('type'),
            price=int(req.POST.get('price')),
        )


    return redirect('/order')

def deleterow(req):

    id = req.GET.get('orderid')
    try:
        CurrentOrder.objects.filter(id=id).delete()

    except Exception as e:
        print(e)
        print("IT Didnt worked")

    return redirect('/')
