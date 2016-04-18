from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
        
class Question(models.Model):
    profile = models.ForeignKey(Profile)
    title = models.CharField(max_length=100)
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Message(models.Model):
    content = models.TextField()
    question = models.ForeignKey(Question)
    from_profile = models.ForeignKey(Profile, related_name='sent')
    to_profile = models.ForeignKey(Profile, related_name='received')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content

class Student(models.Model):
    profile = models.ForeignKey(Profile)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.profile.name
    
class Tutor(models.Model):
    profile = models.ForeignKey(Profile)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.profile.name