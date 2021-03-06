import stripe  

from django.conf import settings
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect  
from django.contrib import messages
from django import forms

stripe.api_key = settings.STRIPE_SECRET_KEY  


class CheckoutPageView(TemplateView):
    template_name = 'checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

#charge view
def charge(request): 
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=2000,
            currency='usd',
            description='DONATE',
            source=request.POST['stripeToken']
        )
    return render(request, 'charge.html')
 
    
    
    
        




