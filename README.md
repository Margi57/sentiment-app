# sentiment-app
## Overview
This project is a simple Django-based API that analyzes the sentiment of text comments using a pre-trained machine learning model. It classifies comments as **positive, negative, or neutral** and provides a confidence score.

## Features
- Django REST API for sentiment analysis
- Text preprocessing and sentiment classification
- Stores sentiment results in a database
- Error handling for empty or very short text

## Technologies Used
- Python
- Django & Django REST Framework
- Postgresql (database)
- Conda for virtual environment

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Margi1703/sentiment-app
cd sentiment_app
```

### 2. Create and Activate Conda Environment
```bash
conda create --name sentiment_app_env python=3.12 -y
conda activate sentiment_app_env
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
(*Ensure `requirements.txt` contains all necessary dependencies, e.g., Django, DRF, scikit-learn, NLTK.*)

### 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Development Server
```bash
python manage.py runserver
```

API will be available at: **http://localhost:8000/api/analyze/**

---

## API Usage
### **Endpoint:**
```
curl --location 'http://localhost:8000/api/analyze/' \
--header 'Content-Type: application/json' \
--data '{
    "text":"Heyy that`s a great news"
}'
```

### **Request Body (JSON):**
```json
{
    "text": "Heyy that`s a great news"
}
```

### **Response:**
```json
{
    "id": 40,
    "text": "Heyy that`s a great news",
    "sentiment": "positive",
    "confidence": 0.62,
    "created_at": "2025-03-03T18:55:38.018399Z"
}
```




