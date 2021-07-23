from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from cart.models import UserOtp,DeliveryAddress,Customer
from cart.models import ExtendedUser
from random import randint
# import twilio
# Create your views here.

def signup(request):
    if request.method == "POST":
        otp = request.POST.get("OTP")
        if otp!=None:
            otp_user = request.POST.get("user")
            #taking username form signup.html and checking if user is present but is not active
            user_now = User.objects.get(username=otp_user)
            if int(otp) == UserOtp.objects.filter(user=user_now).last().otp:
                user_now.is_active = True
                user_now.save()

                messages.success(request, f"Hey {{user.first_name}} your account has been created!")
                return redirect("login")
            else:
                messages.error(request, f"Hey {{user_now.username}} seems like you entered wrong verification code")
                return render(request, "signup.html")

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if not User.objects.filter(username=username,email=email).exists():
                    user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password1
                    )
                    # user.is_active = False
                    user.is_active = False
                    user.save()
                    OTP = str(randint(100000,999999))
                    mobile_num = request.POST.get('mobile_num')
                    check_if_mobile_num_exists = ExtendedUser.objects.filter(mobile_num=mobile_num)

                    if check_if_mobile_num_exists:
                        message.error("Hey this mobile number is taken")
                        return redirect("signup")

                    extended_user = ExtendedUser(user=user, mobile_num=mobile_num)
                    extended_user.save()
                    UserOtp.objects.create(user=user, otp=OTP)
                    mail_mssg = f"Hi {user.first_name},\nYour verification code is {OTP},\nThank You!"
                    send_mail(
                    "Welcome To Mukul Mobiles - Please verify your Email Id to continue",
                    mail_mssg,
                    settings.EMAIL_HOST_USER,
                    [user.email],
                    fail_silently = False
                    )

                    #importing client from twilio.rest
                    # from twilio.rest import Client
                    #
                    # account_sid = 'AC1d8c13ce37accf29c9a8b734546a67f9'
                    # auth_token = 'fd0a360eb1e32ede234802298dcc41b7'
                    # client = Client(account_sid, auth_token)
                    #
                    # message = client.messages.create(
                    #  body=f"Hi {user.first_name} Welcome To Mukul Mobiles,\nYour verification code is {OTP},\nThank You!",
                    #  from_='+14845099394',
                    #  to='+91'+ extended_user.mobile_num
                    # )
                    # return redirect("login")
                    address = request.POST['address']
                    state = request.POST['state']
                    city = request.POST['city']
                    zip_code = request.POST['pincode']


                    del_customer=Customer.objects.create(user=user,name=user.first_name,email=user.email)
                    delivery_address = DeliveryAddress.objects.create(customer=del_customer, address=address, state=state, city=city, zip_code=zip_code)


                    return render(request, "signup.html", {"is_otp_send" : True, "user":user})
            else:
                messages.error(request,"Hey, This email or username is taken!")
                return redirect("signup")
        else:
            messages.error(request,"Hey Passwords doesn't match!")
            return redirect("signup")
    print("in signup")
    return render(request, "signup.html")

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = auth.authenticate(username=username, password=password)
        if user is None or user.email != email:
            messages.info(request,"Invalid username or password!")
            return redirect("login")
        else:
            auth.login(request,user)
            return redirect("/")

    else:
        return render(request,"login.html")


def logout(request):
    auth.logout(request)
    return redirect("/")
