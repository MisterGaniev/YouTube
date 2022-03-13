from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import *
from rest_framework.generics import *
from .serializers import *

# Create your views here.

class MediaCreate(CreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerial
    permission_classes = [IsAuthenticated,]

class MediaDelete(DestroyAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerial
    permission_classes = [IsAuthenticated,]

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerial
    permission_classes = [IsAuthenticated,]


class PlayListViewSet(ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = PlayListSerial
    permission_classes = [IsAuthenticated,]

class LikeCreateList(ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerial
    permission_classes = [IsAuthenticated,]

class LikeDelete(DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerial
    permission_classes = [IsAuthenticated,]

class SavedCreateList(ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = SavedSerial
    permission_classes = [IsAuthenticated,]

class SavedDelete(DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = SavedSerial
    permission_classes = [IsAuthenticated,]
