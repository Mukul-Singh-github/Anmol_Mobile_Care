from django.db import models
from product.models import Mobile,Category
from django.contrib.auth.models import User
# from .category import Category
# Create your models here.


class ExtendedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_num = models.CharField(max_length=15)

    def __str__(self):
        return "User: "+self.user.username + " mobile no: "+self.mobile_num


class UserOtp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.IntegerField()
    otp_sent_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "User: "+self.user.username

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length = 100)
    email = models.EmailField()

    def __str__(self):
        return "Customer Name: " +self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True )
    transaction_id = models.CharField(max_length=50,null=True)
    order_date = models.DateTimeField(auto_now_add=True)

    @property # this is a decorator which let us use this method as a property
    def get_total_price(self):
        total_price = 0
        total_items = self.orderitems_set.all()
        for item in total_items:
            total_price += item.get_quantitywise_price
        return total_price + 60 + 23

    @property
    def get_total_quantity(self):
        item_count = 0
        total_items = self.orderitems_set.all()
        for item in total_items:
            item_count += item.quantity
        return item_count

    # def __str__(self):
    #     print(self.customer)
        # return "Customer: "+self.customer.user

class DeliveryAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.CharField(max_length=250,null=True)
    state = models.CharField(max_length=60,null=True)
    city = models.CharField(max_length=60,null=True)
    zip_code = models.CharField(max_length=10,null=True)
    date_of_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Customer: "+self.customer.name+" Address: "+self.address


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Mobile, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0,null=True)
    order_address = models.ForeignKey(DeliveryAddress, on_delete=models.CASCADE,null=True)

    @property
    def get_quantitywise_price(self):
        return self.product.price * self.quantity

    # def __str__(self):
    #     return "Customer: "+ self.order.customer.name +" "+self.product.brand+" " +self.product.model_no



STATUS_CHOICE= (
                    ("Pending","Pending"),
                    ("Accepted","Accepted"),
                    ("Packed","Packed"),
                    ("On The Way","On The Way"),
                    ("Delivered","Delivered"),
                    ("Canceled","Canceled"),
                )

class PlacedOrder(models.Model):
    customer    = models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True )
    order       = models.ForeignKey(Order,  on_delete=models.CASCADE,null=True)
    product     = models.ForeignKey(Mobile, on_delete=models.CASCADE,null=True )
    order_date  = models.DateTimeField(auto_now_add=True)
    order_status= models.CharField(max_length=100, choices=STATUS_CHOICE, default="Pending")

    def __str__(self):
        return "Order placed: "+str(self.customer)+" " + str(self.order_date)
