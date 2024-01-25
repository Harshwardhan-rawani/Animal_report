from django.shortcuts import render
from django.http import HttpResponse
from feeback_report.models import feedback
import requests
import random
from Photo.models import photo
def index(request):
   search=''
   name=''
   if request.method=="POST":
      search=request.POST.get('search')
      search=search.lower()
   if len(search)==0:
      list_of_animal=['tiger','lion','horse','monkey']
      name=random.choice(list_of_animal)
   if len(search)>0:
      name=search
   
   api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
   response = requests.get(api_url, headers={'X-Api-Key': '7IhSopV9PO7LxdDztrNv0A==mViAU5ZdVucYNZrR'})
   if response.status_code == requests.codes.ok:
      print("ok printed")
   else:
      print("Error:", response.status_code, response.text)
   pic=photo.objects.filter(Name=name).values()
   report_list=response.json()
   pic=photo.objects.filter(Name=name).values()
   new_dict={}
   for i in report_list:
      if (i.get('name').lower()== name):
         new_dict=i
   return render(request,'index.html',{'pic':pic,'report':new_dict} )

def feed(request):
   text=""
   if(request.method=="POST"):
      name=request.POST.get('name')
      email=request.POST.get('email')
      feedback_user=request.POST.get('feed')
      print(name)
      x=feedback(Name=name,Email=email,feedback=feedback_user)
      x.save()
      text="Thank You {}".format(name)
   return render(request,'feedback.html',{'name':text})
   


   
  
