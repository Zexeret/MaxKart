from django.shortcuts import render ,redirect
from .models import ContactUs
from .models import Service
from .models import Haircut


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
        alltype = service[int(id)].objects.all()

        types = service[int(id)].objects.all().values('type').distinct()
        typeid = service[int(id)].objects.all().values('type_id').distinct()

        stypes = {}
        for i in range(len(types)):
            stypes[types[i]['type']] = typeid[i]['type_id']


        params = {'chead' : chead , 'types' : stypes , 'carddetails' : alltype}
        print(params)
        return render(req, "cards.html" , params)

    else:
        return redirect("/")

