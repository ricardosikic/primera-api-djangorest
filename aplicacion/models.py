from django.db import models

# Enter your model

class User(models.Model):
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.IntegerField()
    city = models.CharField(max_length=150)
    about = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title