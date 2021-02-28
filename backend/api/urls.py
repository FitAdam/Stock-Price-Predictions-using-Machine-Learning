from django.urls import path
from .views import ListPost, DetailPost, NewsTitlesView

app_name = 'api'

urlpatterns = [
   # url patterns
    path('post-list', ListPost.as_view(), name='post_list'),
    path('<int:pk>/', DetailPost.as_view()),
    path('news-titles', NewsTitlesView.as_view(), name='news_titles')
    
]

