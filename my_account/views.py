
from my_account.models import UserProfile

from django.contrib import messages

from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from shopping_cart.models import ShoppingCartModel

from .forms import UserProfileForm

from . import models as UPAD

from .models import UserPurchaseHistory as PH

# Create your views here.


class MyAccount(TemplateView):
    template_name = 'my_account/my_account.html'

    """
    GET CLASS
    """

    def get(self, request):
        # CREATE A SESSION IF NOT EXISTING!!

        if not request.session.exists(request.session.session_key):
            request.session.create()
        session_key = request.session.session_key

        current_user = request.user
        if not request.user.is_authenticated:
            return redirect("login_register")

        logged_in=False
        if request.user.is_authenticated:
            logged_in=True
            current_user = request.user

        SCM = ShoppingCartModel.objects.filter(
            cart_owner=current_user).filter(cart_session=session_key)
        basket_item_count = SCM.count

        # GET Correct User
        UPD = UserProfile.objects.filter(up_username=current_user)

        """
        CREATE INITIAL BLANK FORM 
        """
        preload = {

            'username': current_user,
            'email': request.user.email,

        }

        UPF = UserProfileForm(preload)

        c = UserProfile.objects.all().filter(up_username=str(current_user))

        if c:

            """
            LOAD UP USER PROFILE FORM
            """
            preload = {

                'username': current_user,
                'email': UPD[0].up_email,
                'first_name': UPD[0].up_first_name,
                'last_name': UPD[0].up_last_name,
                'address_line1': UPD[0].up_address_line1,
                'address_line2': UPD[0].up_address_line2,
                'address_line3': UPD[0].up_address_line3,
                'post_code': UPD[0].up_post_code,
                'country': UPD[0].up_country,

            }

            UPF = UserProfileForm(preload)

        purchase_history = PH.objects.filter(ph_cart_owner=current_user)

        context = {

            'session_key': session_key,
            'current_user': current_user,
            'basket_item_count': basket_item_count,

            'SCM': SCM,
            'UPF': UPF,
            'purchase_history': purchase_history,
            'logged_in':logged_in,
        }

        return render(request, 'my_account/my_account.html', context)

    """
    POST CLASS  CODE
    """

    def post(self, request):
        # CREATE A SESSION IF NOT EXISTING!!
        if not request.session.exists(request.session.session_key):
            request.session.create()
        session_key = request.session.session_key

        current_user = request.user
        if not request.user.is_authenticated:
            return redirect("login_register")
        
        logged_in=False
        if request.user.is_authenticated:
            logged_in=True
            current_user = request.user

        SCM = ShoppingCartModel.objects.filter(
            cart_owner=current_user).filter(cart_session=session_key)
        basket_item_count = SCM.count

        """
        SAVE PROFILE
        """

        c = UserProfile.objects.all().filter(up_username=str(current_user))
        c.delete()

        b = UPAD.UserProfile(

            up_username=current_user,
            up_first_name=(request.POST['first_name']),
            up_last_name=(request.POST['last_name']),

            up_email=(request.POST['email']),

            up_address_line1=(request.POST['address_line1']),
            up_address_line2=(request.POST['address_line2']),
            up_address_line3=(request.POST['address_line3']),
            up_post_code=(request.POST['post_code']),
            up_country=(request.POST['country']),

        )

        """
        VALIDATE FORM
        """
        if len(b.up_first_name) < 4 or len(b.up_last_name) < 4:
            messages.info(request,
                          'Please Complete The form Properly..\
                              Something seems incorrect in the names section!')
            return redirect('my_account')

        if len(b.up_address_line1) < 1 or len(b.up_address_line2) < 4 or len(b.up_address_line3) < 4:
            messages.info(request,
                          'Please Complete The form Properly..\
                              Something seems incorrect in the address section!')
            return redirect('my_account')

        if len(b.up_post_code) < 4 or len(b.up_country) < 4:
            messages.info(request,
                          'Please Complete The form Properly..\
                              Something seems incorrect in the post-code or country section!')
            return redirect('my_account')

        # OK TO SAVE FORM NOW!!
        b.save()

        messages.info(request, "Your profile has been successfully saved!!")

        preload = {

            'username': current_user,
            'email': request.user.email,

        }

        UPF = UserProfileForm(preload)

     
        context = {

            'session_key': session_key,
            'current_user': current_user,
            'basket_item_count': basket_item_count,

            'SCM': SCM,
            'UPF': UPF,
            'PH': PH,
            'logged_in':logged_in,
        }

        return render(request, 'my_account/my_account.html', context)
