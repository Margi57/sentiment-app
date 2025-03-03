from django.urls import path
from sentiment_app.view.views import SentimentAnalysisView  

# Define URL patterns for the sentiment analysis API
urlpatterns = [
    path('analyze/', SentimentAnalysisView.as_view(), name='sentiment_analysis'),
]
