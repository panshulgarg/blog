from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import Blog,Comment
from .forms import BlogForm , CommentForm
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
	comment=Comment.objects.filter(blog=blogs)
	#hello=1
	number=Comment.objects.filter(blog=blogs).count()
	#for C in blogs:
	#	hello=hello+1

	context={'blog':blogs,'comment':comment,'count':number}
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

@login_required(login_url='/admin/login')
def add_comment_to_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.content = request.POST['content']
            comment.author = request.user
            comment.blog=Blog.objects.get(pk=pk)
            comment.save()
            return HttpResponse("Comment Saved")
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})





