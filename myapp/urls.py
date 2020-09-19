from django.urls import path, include
from rest_framework import routers

from . import views

# authors_list = views.AuthorViewSet.as_view({"get": "list"})
# author_create = views.AuthorViewSet.as_view({"post": "create"})
router = routers.DefaultRouter()

#router.register("authors", views.AuthorView.as_view())

languages_list = views.LanguageViewSet.as_view({"get": "list"})
language_create = views.LanguageViewSet.as_view({"post": "create"})
language_details = views.LanguageViewSet.as_view({"get": "retrieve"})

router.register("languages", views.LanguageViewSet, basename="language")
router.register("posts", views.PostViewSet, basename="post")
urlpatterns = [
    path("", include(router.urls)),
    path("authors", views.AuthorView.as_view(), name="authors"),
    path("authors/<int:id>", views.AuthorDetailView.as_view(), name="authors")
]
