from django.urls import include, path
from django.conf.urls import url
from . import views
from rest_auth.registration.views import (SocialAccountListView, SocialAccountDisconnectView, )



urlpatterns = [
    path("users/", include('users.urls')),
    path("rest-auth/", include('rest_auth.urls')),
    path("rest-auth/registration/", include('rest_auth.registration.urls')),
    url(r'^', include('django.contrib.auth.urls')),
    #social login
    path("rest-auth/facebook/", views.FacebookLogin.as_view(), name="fb_login"),
    path("rest-auth/twitter/", views.TwitterLogin.as_view(), name='twitter_login'),
    path("rest-auth/facebook/connect/", views.FacebookConnect.as_view(), name="fb_connect"),
    path("rest-auth/twitter/connect/", views.TwitterConnect.as_view(), name="twitter_connect"),
    path("rest-auth/google/", views.GoogleLogin.as_view(), name="google_login"),


    #The following views are used to check all social accounts attached to the
    #current authenticated user and disconnect selected social accounts"""

    url(r"^rest-auth/socialaccounts/$", SocialAccountListView.as_view(), name="social_account_list"),
    url(
        r'^socialaccounts/(?P<pk>\d+)/disconnect/$',
        SocialAccountDisconnectView.as_view(),
        name='social_account_disconnect'
    )
]
