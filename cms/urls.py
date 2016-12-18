from django.conf.urls import url
from . import views

urlpatterns=[
	url('^$',views.index,name='index'),
	url('^(?P<pk>[0-9]+)$',views.page,name='page'),
	url('^add$',views.addBlog,name='new'),
	url('^(?P<pk>[0-9]+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),


	]
