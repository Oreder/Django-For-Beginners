# views.py
from django.shortcuts import render, HttpResponse
import requests

# Create your views here.

# ./index
def index(request):
	return HttpResponse('Step 3. index view!')
	
# ./test
def test(request):
	return HttpResponse('Step 3. test view!')