from django.shortcuts import render,redirect
from product.models import Mobile,Image
# Create your views here.

def productDetail(request,mobile_id,cat_id):
    if cat_id == 1: #Mobiles
        mobile = Mobile.objects.get(id=mobile_id)
        images = Image.objects.get(id=mobile_id)
        return render(request, "Product_detail.html", {'mobile':mobile, 'images':images})
    # print("this is mobile",mobiles)
    elif cat_id == 2: #Headphones
        headphone = Mobile.objects.get(id=mobile_id, category_id=cat_id)
        images = Image.objects.get(id=mobile_id)
        return render(request, "headphone.html", {'headphone':headphone, 'images':images})

    elif cat_id == 3: #chargers
        charger = Mobile.objects.get(id=mobile_id, category_id=cat_id)
        images = Image.objects.get(id=mobile_id)
        return render(request, "charger.html", {'charger':charger, 'images':images})

    elif cat_id == 4: #cables
        cable = Mobile.objects.get(id=mobile_id, category_id=cat_id)
        images = Image.objects.get(id=mobile_id)
        return render(request, "cable.html", {'cable':cable, 'images':images})

    elif cat_id == 5: #battery
        other = Mobile.objects.get(id=mobile_id, category_id=cat_id)
        images = Image.objects.get(id=mobile_id)
        return render(request, "accessories.html", {'other':other, 'images':images})
    else:
        mobile = 0
        return redirect("/")
