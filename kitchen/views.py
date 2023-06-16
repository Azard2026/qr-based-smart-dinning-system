from django.shortcuts import render,redirect
from .models import kitchenstaff
from manager.models import orders
import datetime

# Create your views here.

def login(request):
    kitchenstaffs=kitchenstaff.objects.all()
    if request.POST:
        username=request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        for check in kitchenstaffs:
            if check.username==username and check.password==password:
                return redirect('kitchen:dashboard')
            else:
                msg={'msg':"wrong userid and password"}
                return render('kitchen/login.html',msg)

    

    return render(request,'kitchen/index.html')


def dashboard(request):
    
    today=datetime.date.today()
    #print(today)
    order=orders.objects.filter(date=today,cook="pending",cancel='No')
    tab=[]
    for i in order:
        if i.tablenumber not in tab:
            tab.append(i.tablenumber)
    if request.POST:
        table=request.POST.get('table')
       # print(table)
        request.session['delivertab']=table
        stab=request.session['delivertab']
        #print(stab)
       
        billno = []
        day=datetime.date.today()
        orderg=orders.objects.filter(tablenumber=table,date=day,cook="pending",cancel='No')
        for bill in orderg:
            if bill.orderid not in billno:
                billno.append(bill.orderid)
        if request.POST:
            TAB=request.POST.get('ctab')
            BILL=request.POST.get('tabbill')
            cook=[]
            msg=[]
            orderstate=[]
            ordersa=orders.objects.filter(tablenumber=TAB,orderid=BILL,date=day,cook="pending",cancel='No')
            #print(ordersa)
            for item in ordersa:
                if item.cook not in cook:
                    cook.append(item.cook)
                if item.note not in msg:
                    msg.append(item.note)
                if item.orderstatus not in orderstate:
                    orderstate.append(item.orderstatus)
            if request.POST:
                tabcon=request.POST.get('tabcon')
                billcon=request.POST.get('billnocon')
                cookcon=request.POST.get('updatecook')
                print(day)
                print(billcon)
                print(tabcon)
                print(cookcon)
                ordercon=orders.objects.filter(tablenumber=tabcon,orderid=billcon,date=day,cook="pending",cancel='No')
                if ordercon != '':
                    redict=[]
                for con in ordercon:
                    con.cook=cookcon
                    con.save()
                for ors in ordercon:
                    if ors.cook not in redict:

                        redict.append(ors.cook)
                    if redict[0] == 'delivered':                
                        return redirect('kitchen:dashboard')   
                

            ptx={'gettab':TAB,'getbill':BILL,'ordersa':ordersa,'note':msg,'cook':cook,'status':orderstate,'billno':billno,'tab':stab,'table':tab}
            return render(request,'kitchen/dashboard.html',ptx)
        gtx={'billno':billno,'tab':stab,'table':tab}
        return render(request,'kitchen/dashboard.html',gtx)
    else:
        ctx={'table':tab}
        return render(request,'kitchen/dashboard.html',ctx)
def completedorder(request):
    today=datetime.date.today()
    #print(today)
    order=orders.objects.filter(date=today,cook="delivered")
    tab=[]
    for i in order:
        if i.tablenumber not in tab:
            tab.append(i.tablenumber)
    if request.POST:
        table=request.POST.get('table')
        # print(table)
        request.session['deliverctab']=table
        stab=request.session['deliverctab']
        #print(stab)

        billno = []
        day=datetime.date.today()
        orderg=orders.objects.filter(tablenumber=table,date=day,cook="delivered")
        for bill in orderg:
            if bill.orderid not in billno:
                billno.append(bill.orderid)
        if request.POST:
            TAB=request.POST.get('ctab')
            BILL=request.POST.get('tabbill')
            cook=[]
            msg=[]
            orderstate=[]
            ordersa=orders.objects.filter(tablenumber=TAB,orderid=BILL,date=day,cook="delivered")
            #print(ordersa)
            for item in ordersa:
                if item.cook not in cook:
                    cook.append(item.cook)
                if item.note not in msg:
                    msg.append(item.note)
                if item.orderstatus not in orderstate:
                    orderstate.append(item.orderstatus)
            ptx={'gettab':TAB,'getbill':BILL,'ordersa':ordersa,'note':msg,'cook':cook,'status':orderstate,'billno':billno,'tab':stab,'table':tab}
            return render(request,'kitchen/completedorder.html',ptx)
            
        gtx={'billno':billno,'tab':stab,'table':tab}
        return render(request,'kitchen/completedorder.html',gtx)

    ctx={'table':tab}
    return render(request,'kitchen/completedorder.html',ctx)

    