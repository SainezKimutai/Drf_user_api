from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     author = serializers.CharField(max_length=200)
#     email = serializers.EmailField(max_length=200)
#     date = serializers.DateTimeField(auto_now_add=True)
#
#     def create(self, validated_data):
#         return Article.objects.create(validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.author = validated_data.get('author', instance.author)
#         instance.email = validated_data.get('email', instance.email)
#         instance.date = validated_data.get('title', instance.date)
#         instance.save()
#         return instance
