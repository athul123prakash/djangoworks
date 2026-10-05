from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
# def Home(request):
#     if request.method=="GET":
#         return HttpResponse("welcome to Django")


# define index view return message "Index Page

# def Index(request):
#     if request.method=="GET":
#         return HttpResponse("Index Page")

from django.views import View
class Home(View):
    def get(self,request):
        if request.method == "GET":
            return HttpResponse("welcome")

class Index(View):
    def get (view,request):
        if request.method == "GET":
            return HttpResponse("Index")