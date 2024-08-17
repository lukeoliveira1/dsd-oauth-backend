from django.urls import path

from core.api.views import GitHubLogin

urlpatterns = [path("dj-rest-auth/github/", GitHubLogin.as_view(), name="github_login")]
