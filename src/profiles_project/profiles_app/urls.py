from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,base_name='hello-viewset')
router.register('login',views.LoginViewSet,base_name='login-profile')
router.register('profile',views.UserProfileViewSet)
router.register('feed',views.UserProfileFeedViewSet)
#NO NEED TO GIVE BASE NAMES FOR REGTERING MODEL VIEWSETS
urlpatterns = [
    url(r'hello-view/', views.HelloAPIView.as_view()),
    url(r'',include(router.urls))

]
