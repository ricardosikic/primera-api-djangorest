from django.shortcuts import render
from .models import User
from .models import Post
from rest_framework import viewsets
from .serializers import UserSerializer
from .serializers import PostSerializer

# Create your views here.

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    # con queryset te permite leer los datos de una bd
    queryset = Post.objects.all()
    