from rest_framework import generics, viewsets
from .models import Post, NewsTitles
from .serializers import PostSerializer, NewsTitlesSerializers

from django.shortcuts import render
from . forms import NewsTitlesForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import pickle
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd


class ListPost(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DetailPost(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class NewsTitlesView(generics.RetrieveAPIView):
	queryset = NewsTitles.objects.all()
	serializer_class = NewsTitlesSerializers

"""
@api_view(["POST"])
def go_down_or_up(request):
	try:
		
        pickle_open = open("stocks_news_model.pickle", "rb")
       
        randomClassifier = pickle.load(pickle_open)
      
        predictions = randomClassifier.predict(test_dataset)

		mydata = request.data
		unit = np.array(list(mydata.values()))
		unit = unit.reshape(1, -1)
		y_pred = mdl .predict(X)
		y_pred = (y_pred > 0.58)

		newdf = pd.DataFrame(y_pred, columns=['Status'])
		newdf = newdf.replace({True: 'Go Up', False: 'Go Down'})
		return JsonResponse('Your Stock will {} in the long term.'.format(newdf), safe=False)
	except ValueError as e:
		return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
"""