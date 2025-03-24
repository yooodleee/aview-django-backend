from django.urls import path, include
from rest_framework.routers import DefaultRouter

from naver_oauth.controller.naver_oauth_controller import NaverOauthController

router = DefaultRouter()
router.register(r"naver-oauth", NaverOauthController, basename='naver-oauth')

urlpatterns = [
    path('', include(router.urls)),
    path('request-login-url',
         NaverOauthController.as_view({ 'get': 'requestNaverOauthLink' }),
         name='Naver Oauth 링크 요청'),
    path('redirect-access-token',
         NaverOauthController.as_view({ 'post': 'requestAccessToken' }),
         name='Naver Access Token 요청'),
    path('request-user-token',
         NaverOauthController.as_view({ 'post': 'requestUserToken' }),
         name='User Token 요청'),
    #path('logout', KakaoOauthController.as_view({'post': 'dropRedisTokenForLogout'}),
     #   name='drop-redis_service-token-for-logout'),
]