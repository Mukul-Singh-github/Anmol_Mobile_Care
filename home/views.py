from django.shortcuts import render, redirect
from product.models import Mobile,Image,SubCategory,Category
# Create your views here.

def home(request):
    mobiles = Mobile.objects.filter(category_id=1)
    accessories = Mobile.objects.filter(category_id=6)
    categories = Category.objects.all()  #Remember this for accessories dropdown list on navbar
    return render(request,"home.html", {"mobiles":mobiles[:6], "accessories":accessories, "categories":categories[1:]})

def contactPage(request):
    return render(request, "contact.html")

def search(request):
    search_brand=(request.GET["name"]).capitalize()
    mobiles = Mobile.objects.filter(brand=search_brand)
    return render(request, "mobile_page.html", {"mobiles":mobiles})

def mobile_page(request,sub_cat_id=0, min_range=0, max_range=200000):
    if sub_cat_id:
        mobiles = Mobile.objects.filter(category_id=1, subcategory_id = sub_cat_id)
    else:
        mobiles = Mobile.objects.filter(category_id=1)
    subCat = SubCategory.objects.filter(category_id=1)

    if min_range:
        mobiles = list(mobiles)
        i=0
        while i in range(len(mobiles)):
            if mobiles[i].price not in range(min_range,max_range+1):
                mobiles.remove(mobiles[i])
                i-=1
            i+=1
        # print("removed ",mobiles )
    return render(request,"mobile_page.html", {"mobiles":mobiles, "subCats":subCat, "sub_cat_id":sub_cat_id})

def accessory_page(request,cat_id=0, min_range=0, max_range=200000):
    if cat_id:
        accessory = Mobile.objects.filter(category_id=cat_id)
        print("true")
    else:
        headphones = list(Mobile.objects.filter(category_id=2))
        chargers   = list(Mobile.objects.filter(category_id=3))
        cables     = list(Mobile.objects.filter(category_id=4))
        battery    = list(Mobile.objects.filter(category_id=5))
        others     = list(Mobile.objects.filter(category_id=6))
        accessory = headphones + chargers + cables + battery + others
        print("else Exe")

    if min_range:
        accessory = list(accessory)
        i=0
        while i in range(len(accessory)):
            if accessory[i].price not in range(min_range,max_range+1):
                accessory.remove(accessory[i])
                i-=1
            i+=1
    return render(request, "Accessory.html", {"accessory" : accessory,"cat_id":cat_id}, )
