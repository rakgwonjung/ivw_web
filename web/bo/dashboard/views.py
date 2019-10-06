from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ArticleSerializer
from .serializers import AuthorSerializer
from .serializers import ReplySerializer
from .models import Article 
from .models import Author
from .models import Reply

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    #permission_classes = [IsAuthenticated, IsAdmin, IsAccountAdminOrReadOnly]

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    #permission_classes = [IsAuthenticated, IsAdmin, IsAccountAdminOrReadOnly]

class ReplyViewSet(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    #permission_classes = [IsAuthenticated, IsAdmin, IsAccountAdminOrReadOnly]
