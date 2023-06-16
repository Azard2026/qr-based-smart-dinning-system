from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import drink,chaat,milkshack,sandwich,hotdrink,pizza,ourspecial
from manager.models import customercall,tablenumber
import datetime
import itertools
import random
from manager.models import orders
# Create your views here.
def index(request,tab_id):
      
    request.session.set_expiry(0)
    #tablenum = tablenumber.objects.all()
    tablenum= tablenumber.objects.get(pk=tab_id)

    check=tablenum.tablename
    print(check)
    request.session['tabnum'] =check
    tabnum = request.session['tabnum']
    gtx={'table':tabnum}
    # if request.POST:
    #     check=request.POST.get('table')
    #     request.session['tabnum']=check
    #     tabnum = request.session['tabnum']
    #     gtx={'table':tabnum}
    #     for tab in tablenum:
    #         if tab.tablename==tabnum:
    #             print(tabnum)
    #         return redirect('food:menu')
    return render(request,'food/index.html',gtx)

    # print(request.session['order'])

    ctx={'tables':tablenum}
    return render(request, 'food/index.html',ctx)
def menu(request):
    
    request.session.set_expiry(0)
    
    drinks= drink.objects.all()
    chaats = chaat.objects.all()
    milkshacks=milkshack.objects.all()
    hotdrinks=hotdrink.objects.all()
    ourspecials=ourspecial.objects.all()
    sandwichs=sandwich.objects.all()
    pizzas=pizza.objects.all()
    tabnum= request.session['tabnum']
    print(tabnum)
    
    
    ctx = {'drinks': drinks, 'chaats':chaats,'milkshacks':milkshacks,'table':tabnum,'hotdrinks':hotdrinks,'ourspecials':ourspecials,'sandwichs':sandwichs,'pizzas':pizzas}
    # print (ctx)
    return render(request, 'food/menu.html',ctx)

def cart(request):

    
    request.session.set_expiry(0)
    tabnum= request.session['tabnum']
    if tabnum =='':
        return redirect('food:index')   
    gxt={'table':tabnum}
    return render(request, 'food/cart.html',gxt)
@csrf_exempt
def order(request):
    request.session.set_expiry(0)
    tabnum= request.session['tabnum']
    if tabnum =='':
        return redirect('food:index')
   

    gxt={'table':tabnum}
    

    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        
        request.session['order'] = request.POST.get('orders')
        request.session['notes'] = request.POST.get('notes')
        request.session['total'] = request.POST.get('total')
        order =  request.session['order']
        note = request.session['notes']
        total = request.session['total']
        a=open ("order.txt", 'w+')
        for i in order:
            if i != '[' and i != ']' and i!='"':
                if i == ',':

                    a.write('\n')
                else:
                    a.write(i)
        a.close()
        a=open ("order.txt", 'r')
        reads=a.readlines()
        orderss= []
        for i in reads:
            orderss.append(i)
        print (orderss)
        billno = random.randint(1000,9999)
        request.session['billno']=billno
        qtyandorginalprice=[]
        nameandprice =[]
        price=[]
        name=[]
        qty=[]
        for i in range(0,len(orderss)):
            if i%2!=0:
                qtyandorginalprice.append(orderss[i])
            else:
                nameandprice.append(orderss[i])
        for i in range(0,len(nameandprice)):
            if i%2==0:
                
                name.append(nameandprice[i])
            else:
                
                price.append(nameandprice[i])
        for i in range(0,len(qtyandorginalprice)):
            if i%2==0:
                
                qty.append(qtyandorginalprice[i])
        # print(orderss)
        # print(name)
        # print(qty)
        # print(price)

        for (x,y,z) in  zip(name,qty,price):
            # print(x,y,z)
            item=orders(orderid=billno,tablenumber=tabnum,date=datetime.date.today(),itemname=x,itemquantity=y,itemprice=z,total=total,note=note)
            item.save()


        # item=orders(item=orderss,date=datetime.datetime.now(),total=total,notes=note)
        # item.save()
        # a.close()
        #item=orders()

        #print(order)
        # print(notes)


    return render(request, 'food/order.html',gxt)


def success(request):
    request.session.set_expiry(0)
    tabnum= request.session['tabnum']
    if tabnum =='':
        return redirect('food:index')
    billno=request.session['billno']
    total=request.session['total']
    note = request.session['notes']

    order=orders.objects.filter(tablenumber=tabnum,orderid=billno)
    status=[]
    payment=[]
    for i in order:
        if i.orderstatus not in status:
            status.append(i.orderstatus)
        if i.payment not in payment:
            payment.append(i.payment)
    if request.POST:
        tab=request.POST.get('table')
        calls=customercall.objects.all()

        if tab !='':
            for i in calls:
                if i.tablecall == tab:
                    return redirect('food:success')
            else:

                call=customercall(tablecall=tab)
                print(call)
                call.save()
                return redirect('food:success')

        print(tab)
    




    ctx= {'order':order,'table':tabnum,'billno':billno,'total':total,'note':note,'status':status ,'payment':payment}
    return render(request,'food/success.html',ctx)
# def calltable(request):
#     request.session.set_expiry(0)
#     tabnum= request.session['tabnum']
#     if request.POST:
#         tab=request.POST.get('table')

#         print(tab)
#     ctx={'table':tabnum}
#     return render(request,'food/call.html',ctx)
def payment(request):
    request.session.set_expiry(0)
    billno=request.session['billno']
    tabnum= request.session['tabnum']
    mode=''
    if request.POST:
        Paytype=request.POST.get('payment')
        if Paytype=="DEBIT/CREDIT CARD":
           return redirect('food:card')
        else:
            print('cod')
            order=orders.objects.filter(tablenumber=tabnum,orderid=billno,orderstatus="confirm")
            for i in order:
                if i.payment=="notpaid":
                    i.payment="COD/UPI"
                    i.save()
            else:
                return redirect('food:success')



    ctx={'table':tabnum }

    return render(request,'food/payment.html',ctx)
def card(request):
    request.session.set_expiry(0)
    billno=request.session['billno']
    tabnum= request.session['tabnum']
    if request.POST:
        order=orders.objects.filter(tablenumber=tabnum,orderid=billno,orderstatus="confirm")
        for i in order:
            if i.payment=="notpaid" or "COD/UPI":
                i.payment="paid"
                i.save()
        else:
            return redirect('food:success')

    return render(request,'food/card.html')