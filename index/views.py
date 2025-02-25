from django.shortcuts import render
import requests
from .models import Subscription

def subscription_view(request):
    subscriptions = Subscription.objects.all()  
    return render(request, "subscriptions.html", {"subscriptions": subscriptions})
 
def index(request):
   return render(request, 'index.html')

def subscriptions(request):
   return render(request, 'subscriptions.html')

def practice(request):
   return render(request, 'practice.html')

def grammar_page(request):
   return render(request, 'grammar.html')

def dictionary(request):
   return render(request, 'dictionary.html')



