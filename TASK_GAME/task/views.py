
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Word
from .serializers import WordSerializer
from django.shortcuts import render

@api_view(['GET'])
def get_words(request):
    # Fetch all entries in the Words model
    words = Word.objects.all()
    # Serialize the data
    serializer = WordSerializer(words, many=True)
    # Return a JSON response with the serialized data
    return render(request, 'task/words_list.html', {'words': words})  
