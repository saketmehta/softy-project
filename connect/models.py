from django.db import models
from users.models import Profile

# Create your models here.
        
class Question(models.Model):
    profile = models.ForeignKey(Profile)
    title = models.CharField(max_length=100)
    details = models.TextField()
    is_solved = models.BooleanField(default=False)
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