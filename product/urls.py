from django.urls import path,include
from product import views

urlpatterns = [
    path("product_detail/<int:mobile_id>/<int:cat_id>",views.productDetail, name="product_detail"),
    path("cart/",include("cart.urls")),
]
