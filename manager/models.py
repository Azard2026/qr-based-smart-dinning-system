from django.db import models

# Create your models here.

class orders(models.Model):
    orderid = models.IntegerField()
    tablenumber=models.CharField(max_length=25)
    date=models.DateField()
    itemname=models.CharField(max_length=60)
    itemquantity=models.IntegerField()
    itemprice=models.IntegerField()
    total=models.IntegerField()
    orderstatus=models.CharField(max_length=20,default="waiting",blank=True, null=True)
    note = models.CharField(max_length=100, null=True, blank=True )
    cook=models.CharField(max_length=20, default="pending" ,null=True, blank=True )
    cancel=models.CharField(max_length=20,default='No',null=True,blank=True)
    payment=models.CharField(max_length=25,default="notpaid", null=True,blank=True)
    
    # def date_now(self):
    #     return self.time.strftime('%D/%M/%Y %H:%M:%S')

# class orderconform(models.Model):
#     billnumber=models.IntegerField()
#     tableno=models.CharField(max_length=25)
#     itemnames=models.TextField()
#     itemquantitys=models.TextField()
#     itemprices=models.TimeField()
#     itemtotal=models.IntegerField()
#     # dateandtime=models.DateTimeField(auto_now_add=True)
#     # paymenttype=models.CharField(max_length=25,blank=True)
#     # paymentstatus=models.CharField(max_length=25,blank=True)
class customercall(models.Model):
    tablecall=models.CharField(max_length=50,unique=True)

class tablenumber(models.Model):
    tablename = models.CharField(max_length=20)
    def __str__(self):
        return self.tablename
