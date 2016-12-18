from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^users/$', views.BlogList.as_view()),	

]
