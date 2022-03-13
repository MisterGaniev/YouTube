from .models import *
from rest_framework.serializers import ModelSerializer

class MediaSerial(ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'

class PostSerial(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PlayListSerial(ModelSerializer):
    class Meta:
        model = PlayList
        fields = '__all__'

class LikeSerial(ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class SavedSerial(ModelSerializer):
    class Meta:
        model = Saved
        fields = '__all__'
