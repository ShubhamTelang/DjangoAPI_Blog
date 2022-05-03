from rest_framework import serializers
from Blogapp.models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(read_only=True)
    class Meta:
        model = BlogPost
        fields = "__all__"
