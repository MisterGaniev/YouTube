from django.contrib import admin
from django.contrib.admin import ModelAdmin
from main_app.models import *

# Register your models here.

@admin.register(Media)
class Media_admin(ModelAdmin):
    pass


@admin.register(Post)
class Post_admin(ModelAdmin):
    pass

@admin.register(PlayList)
class PlayList_admin(ModelAdmin):
    pass

@admin.register(Like)
class Like_admin(ModelAdmin):
    pass

@admin.register(Saved)
class Saved_admin(ModelAdmin):
    pass


