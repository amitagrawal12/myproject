from django.shortcuts import render
from post.serializers import PostSerializer,CommentSerializer
from rest_framework import status, viewsets
from post.models import *
from post import serializers
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    
# @api_view(['GET','POST'])
# def post(request):
#      if request.method == 'GET':
#           products = Post.objects.all()    
#           serializer = PostSerializer(products, many =True,context ={"request":request})
#           return Response(serializer.data,status = status.HTTP_200_OK)
#      elif request.method == 'POST':
#           serializer = PostSerializer(data = request.data)
#           if serializer.is_valid(raise_exception =True):
#                serializer.save()
#                return Response({"message":"Successfully Created"},status = status.HTTP_201_CREATED)
#           return Response({'message':'not'})






# class PostViewSet(viewsets.ViewSet):
#     def list(self,request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts,many=True)
#         return Response(serializer.data) 
#     def retrieve(self,request,pk=None):
#         queryset = Post.objects.all()
#         post = get_object_or_404(queryset, pk=pk)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)  

# class CommentViewSet(viewsets.ViewSet): 
#     def list(self,request):
#         comments = Comment.objects.all()
#         serializer = CommentSerializer(comments,many=True)
#         return Response(serializer.data)
#     def retrieve(self,request,pk=None):
#         comments = Post.objects.all()
#         comment = get_object_or_404(comments, pk=pk)
#         serializer = CommentSerializer(comment)
#         return Response(serializer.data) 
#     def create(self,request):
#         serializer = CommentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response("not ok data")



