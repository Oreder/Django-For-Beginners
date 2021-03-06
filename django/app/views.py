# views.py
from django.shortcuts import render, HttpResponse
import requests

# Create your views here.

# ./index
def index(request):
	return HttpResponse('Step 3. index view!')
	
# ./profile
def profile(request):
	parsedData = []
	if request.method == 'POST':
		user = request.POST.get('user')
		req = requests.get('https://api.github.com/users/' + user)
		
		jsonList = []
		jsonList.append(req.json())
		
		userData = {}
		for data in jsonList:
			userData['name'] = data['name']
			userData['blog'] = data['blog']
			userData['public_gists'] = data['public_gists']
			userData['public_repos'] = data['public_repos']
			userData['avatar_url'] = data['avatar_url']
			userData['followers'] = data['followers']
			userData['following'] = data['following']
			userData['location'] = data['location']
		
			parsedData.append(userData)
			
	return render(request, './app/profile.html', {'data': parsedData})