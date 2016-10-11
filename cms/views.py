from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Blog
from .forms import BlogForm 
# Create your views here.
def index(request):
	blogs=Blog.objects.all()
	context={'blogs':blogs}
	return render(request,'index.html',context)



def page(request,pk):
	blogs=Blog.objects.get(pk=pk)
	context={'blog':blogs}
	return render(request,'page.html',context)
@login_required(login_url='/admin/login')
def addBlog(request):
	if request.method=='POST':
		form=BlogForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponse("Form Saved")
		else:
			context={'form':form}
			return render(request,'form',context)
	form=BlogForm()
	context={'form':form}
	return render(request,'form',context)



