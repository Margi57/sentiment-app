from django.db import models


# Create comment table to store content in database
class Comment(models.Model):
    SENTIMENT_CHOICES = [
        ('positive', 'Positive'),
        ('neutral', 'Neutral'),
        ('negative', 'Negative'),
    ]

    text = models.TextField()  
    sentiment = models.CharField(max_length=10, choices=SENTIMENT_CHOICES)  # Sentiment classification
    confidence = models.FloatField()  # Confidence score (0 to 1)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of creation

    def __str__(self):
        return f"{self.text[:50]} - {self.sentiment}"
