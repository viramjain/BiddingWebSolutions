from django.db import models
# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    def __str__(self):
        return self.title
class Productdetails(models.Model):
    ptitle=models.CharField(max_length=100)
    pdesc=models.TextField()
    price=models.CharField(max_length=10)
    Image=models.ImageField(upload_to='images')
    pdate=models.DateTimeField(auto_now=True)
    bidstatus=models.BooleanField(default=False)
    biddate=models.DateField(null=True)
    bidst=models.TimeField(null=True)
    bidet=models.TimeField(null=True)
    cat=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.ptitle
class BidEntry(models.Model):
    lname=models.CharField(max_length=100)
    fname=models.CharField(max_length=100)
    useremail=models.CharField(max_length=100)
    amount=models.CharField(max_length=20)
    product_id=models.IntegerField()
    bidtime=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.useremail
class Bidwinner(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    useremail=models.CharField(max_length=100)
    amount=models.CharField(max_length=100,default=0)
    product_id=models.IntegerField()
    bidtime=models.DateTimeField(null=True)
    def __str__(self):
        return self.fname


class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    item_json=models.CharField(max_length=5000)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.CharField(max_length=12)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip_code=models.CharField(max_length=100)
    amount=models.IntegerField(default=0)
    def __str__(self):
        return self.name





