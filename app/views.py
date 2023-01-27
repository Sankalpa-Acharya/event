from django.shortcuts import render
from django.views import View
from .helper import encode
# Create your views here.



class Home(View):
    def get(self,request):
       return render(request,'index.html',{"encoded_text":""})

    def post(self,request):
       message = str(request.POST['msg']).lower()
       encoded_text = encode.encoder(message)
       return render(request,'index.html',{"encoded_text":encoded_text})