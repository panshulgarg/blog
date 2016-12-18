from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import Blog
from .forms import BlogForm 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger





# Create your views here.
def index(request):
	#blogs=Blog.objects.all()
	#context={'blogs':blogs}
	#return render(request,'index.html',context)
	
	blogs=Blog.objects.all()
	paginator=Paginator(blogs,5)
	page=request.GET.get('page')
	try:
		blog=paginator.page(page)
	except PageNotAnInteger:
		blog=paginator.page(1)
	except EmptyPage:
		blog=paginator.page(paginator.num_pages)
	return render(request,'list.html',{'blog':blog})

	



def page(request,pk):
	blogs=Blog.objects.get(pk=pk)
	context={'blog':blogs}
	return render(request,'page.html',context)
@login_required(login_url='/admin/login')
def addBlog(request):
	if request.method=='POST':
		form=BlogForm(request.POST)

		if form.is_valid():
			post=form.save(commit=False)
			post.author=request.user
			post.save()
			send_mail(request.POST.get('title'),request.POST['content'],'vermahardik46@gmail.com',['vermahardik46@gmail.com','panshulgarg@gmail.com'], fail_silently=False,)
			return HttpResponse("Form Saved")
		else:
			context={'form':form}
			return render(request,'form',context)
	form=BlogForm()
	context={'form':form}
	return render(request,'form',context)

def listing(request):
	blogs=Blogs.objects.all()
	paginator=Paginator(blogs,10)
	page=request.GET.get('page')
	try:
		blog=paginator.page(page)
	except PageNotAnInteger:
		blog=paginator.page(1)
	except EmptyPage:
		blog=paginator.page(paginator.num_pages)
	return render(request,'lsit.html',{'blogs':blog})




