from django.urls import path,include
from home import views
from product.views import productDetail


urlpatterns = [
    path('', views.home, name="home"),
    path('contact_page/',views.contactPage, name="contact_page"),
    path('mobilePage/',views.mobile_page,name="mobilePage"),
    path("product_detail/<int:mobile_id>/<int:cat_id>",productDetail, name="product_detail"),
    path('mobilePageByBrand/<int:sub_cat_id>', views.mobile_page, name="mobilePageByBrand"),
    path('mobilePageByPrice/<int:sub_cat_id>/<int:min_range>/<int:max_range>', views.mobile_page, name="mobilePageByPrice"),
    path('allAccessories/', views.accessory_page, name="accessory_page"),
    path('accessoryPageByProduct/<int:cat_id>',views.accessory_page, name="accessoryPageByProduct"),
    path('accessoryPageByPrice/<int:cat_id>/<int:min_range>/<int:max_range>',views.accessory_page, name="accessoryPageByPrice"),
    path('search/',views.search, name="search"),
]
