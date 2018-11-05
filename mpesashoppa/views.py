# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


from mpesa.api.mpesa_express import MpesaExpress as xpress
from mpesa.api.auth import MpesaBase as base
import json
import base64
from datetime import datetime

base = base(env='sandbox', app_key='KyYj2GJGhNqZD9tPVAKmQE0vxQwoAyj4', app_secret='IQAQmsRFEGCrxJOs', sandbox_url='https://sandbox.safaricom.co.ke', live_url='https://safaricom.co.ke')
token = base.authenticate()
money = xpress(env='sandbox', app_key='KyYj2GJGhNqZD9tPVAKmQE0vxQwoAyj4', app_secret='IQAQmsRFEGCrxJOs', sandbox_url='https://sandbox.safaricom.co.ke', live_url='https://safaricom.co.ke')
# Create your views here.
def index(request):
	return render(request, 'mpesashoppa/index.html')

def other(request):
	return render(request, 'mpesashoppa/other.html')

def form_handle(request):
	if request.method == 'POST':	
		business_shortcode = request.POST['business_shortcode']
		# checkout_request_id = request.POST['checkout_request_id']
		amount = request.POST['amount']
		callback_url = 'https://0.0.0.0:8000/callback'
		reference_code = request.POST['reference_code']
		phone_number = request.POST['phone_number']
		description = request.POST['description']
	
	time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	pas = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
	mystring = business_shortcode+pas+time
	passcode = base64.b64encode(b'%s',mystring)
	print(passcode)
	payload = money.stk_push(business_shortcode,passcode,amount,callback_url,reference_code,phone_number,description)
	response = payload
	return render(request, 'mpesashoppa/form_handle.html',{'response' : response})

def callbacks(request):
	results = request.POST.get('something')
	return render(request, 'mpesashoppa/form_handle.html',{'results' : results})