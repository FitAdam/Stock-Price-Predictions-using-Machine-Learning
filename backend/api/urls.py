from django.urls import path
from . import views
from .views import ListPost, DetailPost, news_titles


urlpatterns = [
   # url patterns
    path('post-list', ListPost),
    path('post-list/<int:pk>/', DetailPost),
    path('news-titles', views.news_titles),

]

