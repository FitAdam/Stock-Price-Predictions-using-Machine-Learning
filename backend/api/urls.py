from django.urls import path
from .views import ListPost, DetailPost

app_name = 'api'

urlpatterns = [
   # url patterns
    path('', ListPost.as_view(), name='post_list'),
    path('<int:pk>/', DetailPost.as_view()),
]

