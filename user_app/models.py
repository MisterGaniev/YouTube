from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Account(models.Model):
    full_name = models.CharField(max_length=40)
    bio = models.CharField(max_length=150, blank=True)
    profile_pic = models.FileField(upload_to='profile_pics', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ForeignKey(settings.ACC, on_delete=models.CASCADE, related_name='user_following', null=True, blank=True)
    followers = models.ForeignKey(settings.ACC, on_delete=models.CASCADE, related_name='user_followers', null=True, blank=True)
    def __str__(self):
        return self.full_name
    def followinglar(self):
        return self.followinglar.count()
    def followerlar(self):
        return self.followerlar.count()