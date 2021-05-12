from rest_framework import generics, viewsets
from .models import Post, NewsTitles
from .forms import NewsTitlesForm
from .serializers import PostSerializer, NewsTitlesSerializers

from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

from .rf_classifier import  get_prediction, save_json_to_csv, delete_last_row


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
    Returns new machine learning sentiment prediciton.
    """
    if request.method == 'GET':
        queryset = NewsTitles.objects.all()
        serializer = NewsTitlesSerializers(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        try:

            serializer = NewsTitlesSerializers(data=request.data)
           
            if serializer.is_valid():
                new_request_titels = request.data
                #print(new_request_titels)
                # Parse json and save
                save_json_to_csv(new_request_titels)
                # Return the prediction
                new_prediction = get_prediction()
                # Clear last row in dataset file.
                delete_last_row()
                # save into database
                serializer.save()
                return Response(new_prediction, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

