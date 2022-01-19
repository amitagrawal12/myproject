from django.db.models import fields
from post import models
from rest_framework import serializers
from post.models import Post, Comment
from decimal import Decimal
from rest_framework.reverse import reverse
import pdb


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post','description']    

class PostSerializer(serializers.ModelSerializer):
    posts = CommentSerializer(many=True)
    
    # def create(self, validated_data):
    #     comment_data= validated_data.pop("description")
    #     post = Post.objects.create(**validated_data)
    #     for one in comment_data:
    #         Comment.objects.create(post=post, **one)
    #         return post
   
    class Meta:
        model = Post
        fields = ['title','description','posts']

    






    
  
























