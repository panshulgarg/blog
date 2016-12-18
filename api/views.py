from django.shortcuts import render
from django.http import HttpResponse
from cms.models import Blog
from api.ModelSerializer import BlogSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404



class BlogList(APIView):	
	def get(self, request, format=None):
		blog = Blog.objects.all()
		serializer = BlogSerializer(blog, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = BlogSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


