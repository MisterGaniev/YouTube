from django.conf import settings
from django.db import models

class Media(models.Model):
    media = models.FileField(upload_to="post_file")

class Post(models.Model):
    media = models.ManyToManyField(Media)
    account = models.ForeignKey(settings.ACC, on_delete=models.CASCADE, related_name="account_posts")
    tag = models.ManyToManyField(settings.ACC, blank=True, related_name="account_tags")
    matn = models.CharField(max_length=300,blank=True)
    joy = models.CharField(max_length=300,blank=True)
    vaqt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.account}'

class PlayList(models.Model):
    account = models.ForeignKey(settings.ACC, on_delete=models.CASCADE, related_name="account_post")
    play_media = models.FileField(upload_to="playlist_post")
    tag = models.ManyToManyField(settings.ACC, blank=True, related_name="account_tag")
    matn = models.CharField(max_length=300, blank=True)
    joy = models.CharField(max_length=300, blank=True)
    vaqt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.account},{self.matn}'

class Like(models.Model):
    account = models.ForeignKey(settings.ACC, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    playlist = models.ForeignKey(PlayList, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f'{self.post},{self.playlist}'

class Saved(models.Model):
    account = models.ForeignKey(settings.ACC, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    playlist = models.ForeignKey(PlayList, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f'{self.post},{self.playlist}'
