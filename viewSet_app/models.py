from django.db import models

# Create your models here.


class detail(models.Model):
    name=models.CharField(max_length=20,blank=False)
    address=models.CharField(max_length=20,blank=False)
    email=models.EmailField(max_length=20,blank=False)
    _id=models.AutoField(primary_key=True,editable=False)
    country=models.CharField(max_length=20,blank=False)
    age=models.IntegerField(null=True , blank=True,default=0)
    degree=models.CharField(max_length=20,blank=False)
    dee=models.CharField(max_length=20,null=True)

    class Meta:
        ordering=["country"] 
        verbose_name="testdata"

    # def __str__(self):
    #         return str(self.email)