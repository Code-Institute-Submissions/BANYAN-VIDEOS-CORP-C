from django.shortcuts import redirect, render
from django.views.generic   import TemplateView

from shopping_cart.models   import  ShoppingCartModel
from shopping_cart  import models

from  .forms import ShippingForm

from my_account import models as UPD

# Create your views here.



class Checkout(TemplateView):
    template_name = 'checkout/checkout.html'
    
    
    
    """
    GET CLASSS
    """
    def get(self, request):
        
        # CREATE A SESSION IF NOT EXISTING!!
        if not request.session.exists(request.session.session_key):
            request.session.create()
        session_key = request.session.session_key
        
        current_user = request.user
        if not request.user.is_authenticated: 
            current_user = request.user
            
        if request.user.is_authenticated:
            current_user = request.user
        
 
        SCM = ShoppingCartModel.objects.filter(cart_owner = current_user).filter(cart_session = session_key)
        
        
        # WORKOUT BILL FOR CUSTOMER
        total_to_pay = 0
        for line_items in SCM:
            total_to_pay = total_to_pay + line_items.cart_price_paid
        shipping_charge = 0
        if total_to_pay <30:
            shipping_charge = round((total_to_pay * 10 )/100,2)
        final_bill=round((total_to_pay+shipping_charge),2)
        
  
        
        """
        EXIT PAYMENT IF NOTHING IN BASKET!
        """
        basket_item_count = 0
        for items in SCM:
            basket_item_count = basket_item_count+1
        if basket_item_count < 1 :
            return redirect('shopping_cart')
     
        
        
        """
        PREPOULATE AND INSTANTIATE SHIPPING FORM!!!
        """
        sf_email='cofoedu@gmail.com'
        if request.user.is_authenticated:
            sf_email=request.user.email
        
        
        TID=str(current_user)+':'+str(session_key)
        preload = {
           
           'sf_username':current_user,
           'sf_email':sf_email,
           'sf_transaction_id':TID
           
        }
    
        SF = ShippingForm(preload)
        
       
        """
        POPULATER IF A PROFILE ALREADY EXISTS FOR USER
        """
        userprofile = UPD.UserProfile.objects.filter(up_username = current_user)
        
        if userprofile:
        
            TID=str(current_user)+':'+str(session_key)
            
            preload = {
           
           'sf_username':current_user,
           'sf_email':sf_email,
           'sf_transaction_id':TID,
           
           'sf_address_line1':userprofile[0].up_address_line1,
           'sf_address_line2':userprofile[0].up_address_line2,
           'sf_address_line3':userprofile[0].up_address_line3,
           'sf_post_code':userprofile[0].up_post_code,
           'sf_country':userprofile[0].up_country,
           
            }    
            
        SF = ShippingForm(preload)
       
       
       
       
       
       
       
       
       
  
  
  
  
    
    
        context = {
            
            'basket_item_count': basket_item_count,
            'current_user': current_user,
            'shipping_charge':shipping_charge,
            'final_bill':final_bill,
            
            'SCM':SCM,
            'SF':SF,
            
        }
 
        return render(request, self.template_name, context)
    
    
    
    
    
    
    
    
    
    
    
    
    
    """
    GET CLASS
    """
    def post(self, request):
        
        # CREATE A SESSION IF NOT EXISTING!!
        if not request.session.exists(request.session.session_key):
            request.session.create()
        session_key = request.session.session_key
        
        current_user = request.user
        if not request.user.is_authenticated: 
            current_user = request.user
            
        if request.user.is_authenticated:
            current_user = request.user
        
 
        SCM = ShoppingCartModel.objects.filter(cart_owner = current_user).filter(cart_session = session_key)
        basket_item_count = SCM.count
        
        # WORKOUT BILL FOR CUSTOMER
        total_to_pay = 0
        for line_items in SCM:
            total_to_pay = total_to_pay + line_items.cart_price_paid
        shipping_charge = 0
        if total_to_pay <30:
            shipping_charge = round((total_to_pay * 10 )/100,2)
        final_bill=round((total_to_pay+shipping_charge),2)
        
        
        
        """
        EXIT PAYMENT IF NOTHING IN BASKET!
        """
        basket_item_count = 0
        for items in SCM:
            basket_item_count = basket_item_count+1
        if basket_item_count < 1 :
            return redirect('shopping_cart')
        
        
        
        """
        PREPOULATE AND INSTANTIATE SHIPPING FORM!!!
        """
        sf_email='cofoedu@gmail.com'
        if request.user.is_authenticated:
            sf_email=request.user.email
        
        
        TID=str(current_user)+':'+str(session_key)
        preload = {
           
           'sf_username':current_user,
           'sf_email':sf_email,
           'sf_transaction_id':TID
           
        }
    
        SF = ShippingForm(preload)
 
 

        
        """
        POPULATER IF A PROFILE ALREADY EXISTS FOR USER
        """
        userprofile = UPD.UserProfile.objects.filter(up_username = current_user)
        
        if userprofile:
        
            TID=str(current_user)+':'+str(session_key)
            
            preload = {
           
           'sf_username':current_user,
           'sf_email':sf_email,
           'sf_transaction_id':TID,
           
           'sf_address_line1':userprofile[0].up_address_line1,
           'sf_address_line2':userprofile[0].up_address_line2,
           'sf_address_line3':userprofile[0].up_address_line3,
           
           'sf_post_code':userprofile[0].up_post_code,
           'sf_country':userprofile[0].up_country,
           
            }    
            
        SF = ShippingForm(preload)
    
    
    
    
    
        
    
    
    
        context = {
            'session_key':session_key,
            'basket_item_count': basket_item_count,
            'current_user': current_user,
            'shipping_charge':shipping_charge,
            'final_bill':final_bill,
            
            'SCM':SCM,
            'SF':SF,
            
        }
 
        return render(request, self.template_name, context)