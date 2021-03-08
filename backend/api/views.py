from rest_framework import generics, viewsets
from .models import Post, NewsTitles
from .forms import NewsTitlesForm
from .serializers import PostSerializer, NewsTitlesSerializers

from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response




class ListPost(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DetailPost(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

"""
class NewsTitlesView(viewsets.ModelViewSet):
	queryset = NewsTitles.objects.all()
	serializer_class = NewsTitlesSerializers
"""

@api_view(['GET', 'POST'])
def news_titles(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        queryset = NewsTitles.objects.all()
        serializer = NewsTitlesSerializers(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NewsTitlesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return 
