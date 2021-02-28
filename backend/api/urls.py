from django.urls import path
from .views import ListPost, DetailPost, NewsTitlesView

app_name = 'api'

urlpatterns = [
   # url patterns
    path('post-list', ListPost.as_view(), name='post_list'),
    path('post-list/<int:pk>/', DetailPost.as_view()),
    path('news-titles/<int:pk>/', NewsTitlesView.as_view())
    
]

