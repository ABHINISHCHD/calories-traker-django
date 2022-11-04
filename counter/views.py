from django.shortcuts import render
import json
import requests 
# Create your views here.
def default(request):

    if request.method=="POST":
        query =request.POST.get('food-item')     
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(
            api_url + query, headers={'X-Api-Key': 'SyMgmd3jriqbDadU/zenoQ==xw2GZvSB6UMPf7Ab'})
        try:
            api=json.loads(api_request.content) 
            print(api)
            print("NOthing")
        except Exception as e:
            api='oops there is an error'
            print('hello')
            print(e)

        return render(request,'home.html',{'api':api})
    else:
        return render(request,'home.html')