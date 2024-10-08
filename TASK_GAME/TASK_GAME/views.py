
from rest_framework.response import Response
from rest_framework.decorators import api_view
from task.models import Word
from task.serializers import WordSerializer
from django.shortcuts import render
import random


def get_words(request):
    words = Word.objects.all()
    word_serializer = WordSerializer(words, many=True)
    random_word = random.choice(word_serializer.data) if word_serializer.data else None
    return render(request, 'word.html', {'word': random_word['name']})  
