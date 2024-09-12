from django.db import models

# Create your models here.
class product_master(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    pname=models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.pname
    
class sub_cate(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    pname=models.ForeignKey(product_master,on_delete=models.CASCADE)
    price=models.IntegerField()
    img=models.ImageField(upload_to='image')
    ram=models.IntegerField()
    pmodel=models.CharField(max_length=20)
    
    
    def __str__(self) -> str:
        return self.pname.pname