from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.http import JsonResponse
import json
from home.models import *
from .models import *
# from django.contrib.auth.models import User
# Create your views here.
from random import randint

def addcart(request):
    if request.user.is_authenticated:
        # transaction_id = randint(1111111111,9999999999)
        current_user = User.objects.get(id=request.user.id)
        # customer = request.user.customer
        customer,created=Customer.objects.get_or_create(user=request.user,name=current_user,email=current_user.email)
        order, created = Order.objects.get_or_create(customer=customer)
        mobiles = order.orderitems_set.all()  #items in OrderItems
    else:
        return redirect("/")

    return render(request,"cart.html",{"mobiles":mobiles, "order_obj":order})


# def checkout(request):
#     if request.user.is_authenticated:
#         current_user = User.objects.get(id=request.user.id)
#         # customer = request.user.customer
#         customer,created=Customer.objects.get_or_create(user=request.user,name=current_user,email=current_user.email)
#         order, created = Order.objects.get_or_create(customer=customer)
#         mobiles = order.orderitems_set.all()
#         if request.method == "POST":
#             address = request.POST['address']
#             state = request.POST['state']
#             city = request.POST['city']
#             zip_code = request.POST['zip_code']
#
#             delivery_address = DeliveryAddress.objects.get_or_create(customer=customer, order=order, address=address,state=state, city=city, zip_code=zip_code)
            # print("delivery address created")
    # else:
    #     return redirect("/")
    #
    # return render(request, "checkout.html",{"mobiles":mobiles, "order_obj":order})


def updateCartItem(request):
    data = json.loads(request.body)
    item_id = data['item_id']
    action = data['action']

    current_user = User.objects.get(id=request.user.id)
    customer,created=Customer.objects.get_or_create(user=request.user,name=current_user,email=current_user.email)
    item = Mobile.objects.get(id=item_id)
    order,created = Order.objects.get_or_create(customer=customer)
    orderItem,created = OrderItems.objects.get_or_create(order=order, product=item)

    if action == "add" or action == "buy":
        orderItem.quantity += 1
    elif action == "remove":
        orderItem.quantity -= 1
    elif action == "delete":
        orderItem.quantity = 0

    else:
        print("else was followed no action chosen")

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse({"action":action}, safe=False)


def afterPayment(request):
    # user = request.GET.get("user")print("inside Inapprove")
    current_user = User.objects.get(id=request.user.id)
    customer=Customer.objects.get(user=current_user,email=current_user.email)
    order = Order.objects.get(customer=customer)
    orderItems = [product for product in OrderItems.objects.filter(order=order)]
    for prod in orderItems:
        PlacedOrder(customer=customer, order=order, product=prod.product).save()
        prod.delete()
    return redirect("myorder")

def myorder(request):
    current_user = User.objects.get(id=request.user.id)

    customer,created=Customer.objects.get_or_create(user=request.user,name=current_user,email=current_user.email)
    placed_orders = PlacedOrder.objects.filter(customer=customer)
    return render(request, "myorder.html",{"placed_orders":placed_orders})
