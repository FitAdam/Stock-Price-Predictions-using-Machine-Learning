from rest_framework import serializers
from .models import Post, NewsTitles


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('author','title','updated','body')

class NewsTitlesSerializers(serializers.ModelSerializer):
    class Meta:
        model = NewsTitles
        fields='__all__'