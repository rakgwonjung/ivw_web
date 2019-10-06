from dashboard.models import Article
from dashboard.models import Author
from dashboard.models import Reply
from rest_framework import serializers

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article 
        fields = ('id', 'title', 'content', 'author', 'replies')

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author 
        fields = ('id', 'nick_name', 'mail')

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply 
        fields = ('id', 'article', 'content', 'author')

