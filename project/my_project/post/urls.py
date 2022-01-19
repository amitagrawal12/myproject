from django.urls import path,include
from .views import PostViewSet,CommentViewSet
from rest_framework.routers import SimpleRouter,DefaultRouter
from rest_framework import routers
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('post', PostViewSet, basename='posts')
posts_router = routers.NestedSimpleRouter(router, 'post',lookup = 'posts')
posts_router.register('comments',CommentViewSet , basename='comments')
urlpatterns = [
path('',include(router.urls)),
path('',include(posts_router.urls)),
path('comments/',CommentViewSet.as_view({"get":"list","post":"create"}))

  ]



# from post import views
# router = DefaultRouter()
# router.register('post',views.PostViewSet,basename='post')  

# router2 = DefaultRouter() 
# router2.register('comment',views.CommentViewSet,basename='comment') 

# urlpatterns = [
#     path("post",include(router.urls)),
#     path("comment/",include(router2.urls)),
   
# ]
