from django.conf.urls import url
from . import views

urlpatterns=[
	url('^$',views.index,name='index'),
	url('^(?P<pk>[0-9]+)$',views.page,name='page')
	]
