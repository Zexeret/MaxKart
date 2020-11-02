from django.shortcuts import render,redirect
from crudapp.models import Customer



def home(req):
    return render(req, "home.html")

def base(req):
    return render(req, "cards page.html")


def order(req):
    if req.method == "POST":

        try:
            # print(req.POST)
            # cname = req.POST.get('cname', "ghgh")
            # print(cname)
            # cnumber = int(req.POST.get('cnumber',"ghgh"))
            # print(cnumber)
            # cemail =req.POST.get('cemail',"ghgh")
            # print(cemail)
            # caddress = req.POST.get('caddress',"ghgh")
            # print(caddress)
            # cservice = req.POST.get('cservice',"ghgh")
            # print(cservice)
            # cprice = int(req.POST.get('cprice',"ghgh"))
            # print(cprice)
            print(req.POST)

            Customer.objects.create(
                cname= req.POST.get('cname',"ghgh"),
            cnumber = int(req.POST.get('cnumber',"ghgh")),
            cemail =req.POST.get('cemail',"ghgh"),
            caddress = req.POST.get('caddress',"ghgh"),
            cservice = req.POST.get('cservice',"ghgh"),
            cprice = int(req.POST.get('cprice',"ghgh"))
            )
            print("IT Worked!!!")
            return redirect("/")
        except:
            print("IT SUChhjKED!!!!!!")
            return redirect("/")

    else:
        print(req.GET)
        price = req.GET.get('price', 100)
        type = req.GET.get('type' , 'Hair')
        return render(req , "order.html" , {'price':price , 'type' : type})
























#
#
#
# def customer(req):
#     if req.method == "POST":
#         form = CustomerForm(req.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 print("YES I m HERE")
#                 return redirect('/show')
#             except:
#                 pass
#     else:
#         form = CustomerForm()
#
#     return render(req,"custo.html",{'form':form})
#
# def show(req):
#     customers = Customer.objects.all() ;
#
#     return render(req , "show.html" , {'customers':customers})
#
# def edit(req , id):
#     customer = Customer.objects.get(id = id)
#     return render(req,"edit.html" ,{'customer': customer})
#
# def update(req,id):
#     customer = Customer.objects.get(id=id)
#     form = CustomerForm(req.POST , instance=customer)
#     if form.is_valid():
#         form.save()
#         return redirect('/show')
#
#     return render(req,"edit.html" ,{'customer': customer})
#
# def delete(req, id):
#     customer = Customer.objects.get(id=id)
#     customer.delete()
#     return redirect("/show")