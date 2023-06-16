from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from .models import tablenumber
from .models import orders,customercall
import datetime
from datetime import date,timedelta
from django.contrib import messages
import qrcode
from fpdf import FPDF
from django.db.models import Q

from io import BytesIO
# Create your views here.
def index(request):

    if request.POST:
        user = request.POST.get('username')
        pwd =request.POST.get('password')
        print(user)
        print(pwd)
        user = authenticate(request, username=user,password=pwd)
        if user is not None:
            login(request, user)
            return redirect('manager:dashboard')
        else:
            messages.info(request,'username and password are incorrect')
    ctx= {'active_link': 'login'}
    
    return render(request,'manager/index.html',ctx)


def logOut(request):
    logout(request)
    return redirect('manager:index')


def dashboard(request):
    tablecall=customercall.objects.all()
    if request.GET:

        call=request.GET.get('call')
        print(call)
        print(call)
        if call != '':

            calls=customercall.objects.get(tablecall=call)
            calls.delete()
            return redirect('manager:dashboard') 
    table=tablenumber.objects.all()
    today=datetime.date.today()
    order=orders.objects.filter(date=today,orderstatus="waiting")
    tab=[]
    for order in order:
        if order.tablenumber not in tab:
            tab.append(order.tablenumber)
    print(tab)
    if request.POST:
        tabs=request.POST.get('tab')
        print (tabs)
        today=datetime.date.today()
        billno=[]
        status=[]
        total=[]
        # itemname=[]
        # itemquantity=[]
        # itemprices=[]
        itemtotal=[]
        note=[]
        cook=[]

        orderss=orders.objects.filter(tablenumber=tabs, date=today,orderstatus="waiting")
        for i in orderss:
            if i.orderid not in billno:
                billno.append(i.orderid)
            if i.total not in total:
                total.append(i.total)
            if i.orderstatus not in status:
                status.append(i.orderstatus)
            if i.note not in note:
                note.append(i.note)
            if i.cook not in cook:
                cook.append(i.cook) 
       # print(billno[0])
        #orderone =orders.objects.filter(tablenumber=tabs, date=today,orderstatus="waiting")
        if request.POST:
            tableno=request.POST.get('tableno')
            bill=request.POST.get('bill')
            if bill == '':
                return redirect('manager:dashboard')
            state=request.POST.get('state')
            print(tableno)
            print(bill)
            print(state)
            today=datetime.date.today()
            orderc=orders.objects.filter(tablenumber=tableno,orderid=bill, date=today)
            if orderc != '':
                redict=[]
           
            for ord in orderc:
                ord.orderstatus=state
                ord.save()
            for ors in orderc:
                if ors.orderstatus not in redict:

                    redict.append(ors.orderstatus)

                if redict[0] == 'confirm':                
                    return redirect('manager:dashboard')    
                  

        gtx={'orders':orderss,'table':tab,'billno':billno,'tableno':tabs,'status':status,'total':total,'note':note,'cook':cook} 
        return render(request,'manager/dashboard.html',gtx)

    
    ctx={'table':tab,'tablecall':tablecall}
    return render(request,'manager/dashboard.html',ctx)


def conformorder(request):
    today=datetime.date.today()
    order=orders.objects.filter(date=today,orderstatus="confirm")
    tab=[]
    for order in order:
        if order.tablenumber not in tab:
            tab.append(order.tablenumber)
    print(tab)
    if request.POST:
        tabs=request.POST.get('tab') 
        # print(tabs)
        request.session['conformtablenumber']=tabs
        table=request.session['conformtablenumber']
        billno=[]
        print(table)
        today=datetime.date.today()
        orderc=orders.objects.filter(tablenumber=table,date=today,orderstatus="confirm")
        for bill in orderc:
            if bill.orderid not in billno:
                billno.append(bill.orderid)
        if request.POST:
            tabl=request.POST.get('tabs')
            bills=request.POST.get('bills')
            
            print(tabl)
            print(bills)
            print(billno)
            if bills == '':
                return redirect('manager:conformorder')
            status=[]
            total=[]
            payment=[]
            cook=[]
            paidstate=['notpaid','COD/UPI']
            orderco=orders.objects.filter(tablenumber=tabl,orderid=bills,date=today,orderstatus="confirm")
            print(orderco)
            for i in orderco:
                if i.orderstatus not in status:
                    status.append(i.orderstatus)
                if i.total not in total:
                    total.append(i.total)
                if i.payment not in payment:
                    payment.append(i.payment)
                if i.cook not in cook:
                    cook.append(i.cook)
            if request.POST:
                canceltab=request.POST.get('cancelordtab')
                cancelbill=request.POST.get('cancelordcbill')

                
                print(canceltab,cancelbill)
                ordercan=orders.objects.filter(tablenumber=canceltab,orderid=cancelbill,date=today)
                for ordd in ordercan:
                    ordd.orderstatus = 'cancelled'
                    ordd.cancel="Yes"
                    ordd.save()
                if request.POST:
                    completetab=request.POST.get('paidtab')
                    completebill=request.POST.get('paidbill')
                    completepaid=request.POST.get('completedpaid')
                    print(completetab,completebill,completepaid)
                    orderpaid=orders.objects.filter(tablenumber=completetab,orderid=completebill,date=today)
                    for ordd in orderpaid:
                        ordd.payment=completepaid
                        ordd.save()

            
            ptx={'tableno':table,'bills':billno,'table':tab,'cpayment':payment,'ctotal':total,'cstatus':status,'corder':orderco,'cbill':bills,'tabl':tabl,'ccook':cook,'cpaid':paidstate}
            return render(request,'manager/orders.html',ptx)


        gtx={'tableno':table,'bills':billno,'table':tab }
        return render(request,'manager/orders.html',gtx)
        



    ctx={'table':tab}

    return render(request,'manager/orders.html',ctx)

def summary(request):
    
    day=datetime.datetime.today()
    if request.POST:
        getday=request.POST.get('Yesterday')
        getweek=request.POST.get('Week')
        getmonth=request.POST.get('month')
        gettab=request.POST.get('table')
        print(getweek)
        print(getday)
        if getday == 'Yesterday':
            yesterdaybill=[]
            today=date.today()
            yesterday=today - timedelta(days=1)
            yesterdayorder=orders.objects.filter(Q(date=yesterday),payment="paid",cancel="No")
            for i in yesterdayorder:
                if i.orderid not in yesterdaybill:
                    yesterdaybill.append(i.orderid)
            
            yesterdaybill=len(yesterdaybill)

            # print(weekorder)
            # print(week)
            yesterdaytotal=0
            yesterdayitemname=[]
            yesterdayitemquantity=[]
            yesterdayitemprice=[]
            
            for i in yesterdayorder:
                yesterdaytotal+=i.itemprice
                if i.itemname not in yesterdayitemname:
                    yesterdayitemname.append(i.itemname)
            
            for item in yesterdayitemname:
                quantity=0
                price=0
                for j in yesterdayorder:
                    if j.itemname==item:
                        quantity+=j.itemquantity
                        price+=j.itemprice
                yesterdayitemquantity.append(quantity)
                yesterdayitemprice.append(price)        
                        
            #print(itemname)
            #print(itemquantity)
            #print(itemprice)
            yesterdayorderss=zip(yesterdayitemname,yesterdayitemquantity,yesterdayitemprice)
            ctx={'yesterdaytotal':yesterdaytotal,'yesterdayorder':yesterdayorderss,'yesterdaybill':yesterdaybill}
            return render(request,'manager/summary.html',ctx)
        elif getweek == 'Week' :
            weekbill=[]
            today=date.today()
            start_of_week=today - timedelta(days=today.weekday())
            end_of_week=start_of_week+timedelta(days=6)
            weekorder=orders.objects.filter(Q(date__gte=start_of_week) & Q(date__lte=end_of_week),payment="paid",cancel="No")
            print(weekorder)
            # print(week)
            for i in weekorder:
                if i.orderid not in weekbill:
                    weekbill.append(i.orderid)
            print(weekbill)
            tweekbill=len(weekbill)
            weektotal=0
            weekitemname=[]
            weekitemquantity=[]
            weekitemprice=[]
            
            for i in weekorder:
                weektotal+=i.itemprice
                if i.itemname not in weekitemname:
                    weekitemname.append(i.itemname)
            
            for item in weekitemname:
                quantity=0
                price=0
                for j in weekorder:
                    if j.itemname==item:
                        quantity+=j.itemquantity
                        price+=j.itemprice
                weekitemquantity.append(quantity)
                weekitemprice.append(price)        
                        
            #print(itemname)
            #print(itemquantity)
            #print(itemprice)
            weekorderss=zip(weekitemname,weekitemquantity,weekitemprice)
            ctx={'weektotal':weektotal,'weekbill':tweekbill,'weekorder':weekorderss}
            return render(request,'manager/summary.html',ctx)
        elif getmonth == 'Month' :
            monthbill=[]
            now = datetime.datetime.now()
            month = now.month
            year = now.year
            print(month)
            print(year)
            monthorder=orders.objects.filter(date__year=year, date__month=month,payment="paid",cancel="No")
            # print(weekorder)
            # print(week)
            for i in monthorder:
                if i.orderid not in monthbill:
                    monthbill.append(i.orderid)
            # print(weekbill)
            tmonthbill=len(monthbill)
            monthtotal=0
            monthitemname=[]
            monthitemquantity=[]
            monthitemprice=[]
            
            for i in monthorder:
                monthtotal+=i.itemprice
                if i.itemname not in monthitemname:
                    monthitemname.append(i.itemname)
            
            for item in monthitemname:
                quantity=0
                price=0
                for j in monthorder:
                    if j.itemname==item:
                        quantity+=j.itemquantity
                        price+=j.itemprice
                monthitemquantity.append(quantity)
                monthitemprice.append(price)        
                        
            #print(itemname)
            #print(itemquantity)
            #print(itemprice)
            monthorderss=zip(monthitemname,monthitemquantity,monthitemprice)
            mctx={'monthtotal':monthtotal,'monthbill':tmonthbill,'monthorder':monthorderss}
            return render(request,'manager/summary.html',mctx)
        elif gettab == 'Table':
            taborder=orders.objects.filter(date=day,payment="paid",cancel="No")
            tab=[]
            for tn in taborder:
                if tn.tablenumber not in tab:
                    tab.append(tn.tablenumber) 
            tabamt=[]
            for i in tab:
                tabs=orders.objects.filter(tablenumber=i,date=day,payment="paid",cancel="No")
                tabtot=0
                for j in tabs:
                    tabtot+=j.itemprice
                # tabtot=tabs.aaggregate(sum(itemprice))
                tabamt.append(tabtot)
            tabwisetot=zip(tab,tabamt)
            tabtxt={'tabtot':tabwisetot}
            return render(request,'manager/summary.html',tabtxt)

        


    order=orders.objects.filter(date=day,payment="paid",cancel="No")
    todaybill=[]
    total=0
    itemname=[]
    itemquantity=[]
    itemprice=[]
    for i in order:
          if i.orderid not in todaybill:
             todaybill.append(i.orderid)
            
    ttodaybill=len(todaybill)
    for i in order:
        total+=i.itemprice
        if i.itemname not in itemname:
            itemname.append(i.itemname)
    
    for item in itemname:
        quantity=0
        price=0
        for j in order:
            if j.itemname==item:
                quantity+=j.itemquantity
                price+=j.itemprice
        itemquantity.append(quantity)
        itemprice.append(price)        
                
    #print(itemname)
    #print(itemquantity)
    #print(itemprice)
    orderss=zip(itemname,itemquantity,itemprice)
    

    gtx={'total':total,'orders':orderss,'todaybill':ttodaybill}
    return render(request,'manager/summary.html',gtx)
def qrgenerator(request):
    table=tablenumber.objects.all()
    if request.POST:
        tabid=request.POST.get('tabid')
        tabname=request.POST.get('tabname')
        url='http://192.168.166.227:8000/tableno:'+str(tabid)
        qr=qrcode.QRCode(version=1,box_size=10, border=4)
        qr.add_data(url)
        qr.make(fit=True)
        img=qr.make_image(fill_color="black",back_color="white")
        buffer= BytesIO()
        img.save(buffer,format='PNG')
        img.save('manager/static/manager/qr/code.png')
        fpdf= FPDF()
        ## add a blank page to the pdf document
        fpdf.add_page()
        fpdf.image("manager/static/manager/image/chan.png",5,5,w=50,h=50)
        # change color
        fpdf.set_text_color(255,0,0)
        ## SET FONT
        fpdf.set_font("Arial",size=50)
        ###add image to pdg
        fpdf.image("manager/static/manager/qr/code.png",50,50,w=100)
        ## add text
        fpdf.text(50,50,txt=tabname)
        fpdf.output("manager/static/manager/qr/qr.pdf")
        gtx={'table':table,'qrtab':tabname}
        return render(request,'manager/qrgenerator.html',gtx)

    gtx={'table':table}
    return render(request,'manager/qrgenerator.html',gtx)
