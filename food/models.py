from django.db import models

# Create your models here.
class drink(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField()
    jImage = models.ImageField(upload_to='juices/') 
 
class pizza(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField()
    iImage = models.ImageField(upload_to='pizza/') 


class milkshack(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField()
    mImage = models.ImageField(upload_to='milkshacks/') 

class chaat(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField()
    cImage = models.ImageField(upload_to='chaat/') 

class sandwich(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField()
    wImage = models.ImageField(upload_to='sandwich/') 



class ourspecial(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField()
    oImage = models.ImageField(upload_to='ourspecial/') 
    


class hotdrink(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField()
    hImage = models.ImageField(upload_to='hotdrinks/') 

# class orders(models.Model):
#     item=models.CharField(max_length=100000)
#     date=models.DateTimeField()
#     total=models.IntegerField()
#     notes=models.CharField(max_length=350)
#     def date_now(self):
#         return self.time.strftime('%d/%m/%Y %H:%M:%S')
    

# class tablenumber(models.Model):
#     tablename = models.CharField(max_length=20)


