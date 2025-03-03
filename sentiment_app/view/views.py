from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..model.models import Comment
from ..serializers.serializers import CommentSerializer
from ..utils.utils import analyze_sentiment

class SentimentAnalysisView(APIView):
    def post(self, request):
        text = request.data.get("text", "")

        # Error handling
        if not text.strip():
            return Response({"error": "Text cannot be empty"}, status=status.HTTP_400_BAD_REQUEST)
        if len(text.split()) < 3:
            return Response({"error": "Text must be at least 3 words"}, status=status.HTTP_400_BAD_REQUEST)

        # Perform sentiment analysis
        sentiment, confidence = analyze_sentiment(text)

        # Store result in database
        comment = Comment.objects.create(text=text, sentiment=sentiment, confidence=confidence)

        # Serialize and return response
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
