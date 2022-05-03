from Blogapp import models
from Blogapp.api.serializers import BlogPostSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from Blogapp.models import BlogPost
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

class allpost(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        post = BlogPost.objects.all()
        serializer = BlogPostSerializer(post,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class post(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        if request.method == 'GET':
            try:
                post = BlogPost.objects.get(pk=pk)
            except BlogPost.DoesNotExist:
                return Response({'Error':'Post not found'},status=status.HTTP_404_NOT_FOUND)
            serializer = BlogPostSerializer(post)
            return Response(serializer.data)

    def put(self,request,pk):
        post = BlogPost.objects.get(pk=pk)
        serializer= BlogPostSerializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        post= BlogPost.objects.get(pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
