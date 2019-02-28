from django.shortcuts import render

#social login facebook
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter 
from rest_auth.registration.views import SocialLoginView
#social login twitter
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter 
from rest_auth.social_serializers import TwitterLoginSerializer

#social login google
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

#Social connect view
from rest_auth.registration.views import SocialConnectView 
from rest_auth.social_serializers import TwitterConnectSerializer


#views

#Google login
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client


#facebook login view
class FacebookLogin(SocialLoginView): 
    adapter_class = FacebookOAuth2Adapter


#twitter login view
class TwitterLogin(SocialLoginView):
    serializer_class = TwitterLoginSerializer 
    adapter_class = TwitterOAuthAdapter

#additional Social Connect Views
"""These views allow connecting existing accounts in addition to login"""

class FacebookConnect(SocialConnectView): 
    adapter_class = FacebookOAuth2Adapter

class TwitterConnect(SocialConnectView): 
    serializer_class = TwitterConnectSerializer 
    adapter_class = TwitterOAuthAdapter


