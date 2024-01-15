from django.urls import path

from . import views

app_name = "helpdesk"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:article_slug>/", views.article, name="article"),
    path('/search_articles/', views.search_articles, name='search_articles'),
]
