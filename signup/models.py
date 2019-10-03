from django.db import models

class details(models.Model):
    firstName=models.CharField(max_length=25)
    lastName=models.CharField(max_length=20)
    phone=models.IntegerField()
    gender=models.CharField(max_length=10)
    email=models.EmailField(unique=True,null=False)
    username=models.CharField(primary_key=True,null=False,max_length=20)
    password=models.CharField(max_length=12,null=False)

    def __str__(self):
        return self.firstName

class foodItem(models.Model):
    name=models.CharField(max_length=15)
    typeof=models.CharField(max_length=15)
    price=models.IntegerField()
    img=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class cart(models.Model):
    name=models.CharField(max_length=15)
    typeof=models.CharField(max_length=15)
    price=models.IntegerField()
    quantity=models.IntegerField()
    transcid=models.CharField(max_length=40,default='NULL')

    def __str__(self):
        return self.name


class transactions(models.Model):
    total=models.IntegerField()
    transactionId=models.CharField(max_length=40)

    def __str__(self):
        return self.transactionId

    
