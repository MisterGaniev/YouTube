from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user_app.views import *
from main_app.views import *

                    # Swagger Documentation
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="YouTube clone API",
      default_version='v1',
      description="The clone version of Netflix.In this project was used with Django Framework and db.sqlite3.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact("Ganiev Xurshidbek contact@snippets.local, <+998916512061>"),
   ),
   public=True,
)

router = DefaultRouter()
router.register('post', PostViewSet),
router.register('playlist', PlayListViewSet),


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/<int:pk>/', UserGetDeleteUpdate.as_view()),
    path('media/<int:pk>/', MediaDelete.as_view()),
    path('like/<int:pk>/', LikeDelete.as_view()),
    path('saved/<int:pk>/', SavedDelete.as_view()),
    path('user/', UserCreateList.as_view()),
    path('media/', MediaCreate.as_view()),
    path('like/', LikeCreateList.as_view()),
    path('saved/', SavedCreateList.as_view()),
    path('get-token/', TokenObtainPairView.as_view()),
    path('refresh-token/', TokenRefreshView.as_view()),
    path('', include(router.urls)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-doc')
]

