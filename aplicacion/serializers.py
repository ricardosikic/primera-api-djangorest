from rest_framework import serializers
from .models import User
from .models import Post

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ('name', 'last_name', 'age', 'city', 'about')
        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'description', 'created_by', 'pub_date')
