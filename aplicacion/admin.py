from django.contrib import admin
from .models import User
from .models import Post

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'age', 'city', 'about')
    

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_by', 'pub_date')
    

admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)    