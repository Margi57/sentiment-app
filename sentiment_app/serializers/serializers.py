from rest_framework import serializers
from ..model.models import Comment

# Serializer for the Comment model

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'sentiment', 'confidence', 'created_at']
