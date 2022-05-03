from rest_framework import serializers
from Blogapp.models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(read_only=True)
    class Meta:
        model = BlogPost
        fields = "__all__"

# class BlogPostSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author_name = serializers.CharField(read_only=True)
#     title = serializers.CharField()
#     body = serializers.CharField()
#     created_at = serializers.DateTimeField()
#     updated_at = serializers.DateTimeField()
#
#     def create(self,validated_data):
#         return BlogPost.objects.create(**validated_data)
#
#     def update(self,instance,validated_data):
#         instance.title = validated_data.get('title',instance.title)
#         instance.body = validated_data.get('body',instance.body)
#         instance.created_at = validated_data.get('created_at',instance.created_at)
#         instance.updated_at = validated_data.get('updated_at',instance.updated_at)
#         instance.save()
#         return instance
