from django.urls import path,include
from cart import views


urlpatterns = [
    path('cart/',views.addcart,name="cart"),
    # path('checkout',views.checkout, name="checkout"),
    path('myorder',views.myorder, name="myorder"),
    path('afterPayment/',views.afterPayment, name="afterPayment"),
    path('accounts/', include("accounts.urls")),

]
