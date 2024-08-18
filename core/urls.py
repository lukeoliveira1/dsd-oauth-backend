from django.urls import path

from core.api.views import (
    GitHubLogin,
    GoogleLogin,
    TestAccessTokenView,
)

urlpatterns = [
    path("dj-rest-auth/github/", GitHubLogin.as_view(), name="github_login"),
    path("dj-rest-auth/google/", GoogleLogin.as_view(), name="google_login"),
    # token
    path("token/get-user/", TestAccessTokenView.as_view(), name="test-token"),
]
