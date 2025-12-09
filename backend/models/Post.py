from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.CharField(max_length=50)
    content = models.TextField()
    scheduled_time = models.DateTimeField(null=True, blank=True)
    published = models.BooleanField(default=False)
    engagement_rate = models.FloatField(default=0.0)
    likes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.platform} - {self.content[:50]}"
