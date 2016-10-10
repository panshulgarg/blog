from django.shortcuts import render
from django.http import HttpResponse

from .models import Blog

# Create your views here.
def index(request):
	blogs=Blog.objects.all()
	context={'blogs':blogs}
	return render(request,'index.html',context)



def page(request,pk):
	blogs=Blog.objects.get(pk=pk)
	context={'blog':blogs}
	return render(request,'page.html',context)
