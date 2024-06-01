# from django.db import models

# Create your models here.
from django.db import models


class contacts(models.Model):
    email = models.EmailField()         
    name = models.CharField(max_length=200)
    # name=models.CharField(max_length=600)
    address= models.CharField(max_length=500)
    address2= models.CharField(max_length=500)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    Zip=models.IntegerField()
    def __str__(self):
        return self.name
class login(models.Model):   
    emails=models.EmailField()
    passwords=models.CharField(max_length=500)
    def __str__(self):
        return self.emails+"-"+self.passwords
#    pub_date = models.DateTimeField('date published')
#    question_text = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('date published')
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


    
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)    