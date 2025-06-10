import pandas as pd
from transformers import pipeline

# Set up the sentiment analysis model
sentiment_model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def Analyze_Sentiment(texts):
    results = sentiment_model(list(texts))
    labels = [r['label'].lower() for r in results]
    scores = [r['score'] for r in results]
    return labels, scores

def sentiment_ADD(Clean, text_col="Review"):
    if text_col not in Clean.columns:
        raise ValueError(f"Column '{text_col}' not found in DataFrame.")

    # Convert to string
    Clean[text_col] = Clean[text_col].astype(str)

    labels, scores = Analyze_Sentiment(Clean[text_col].tolist())  # Convert to list
    Clean["sentiment_label"] = labels
    Clean["sentiment_score"] = scores
    return Clean

def Combine_sentiment(Clean, by=["Bank", "Rating"]):
    return Clean.groupby(by)[["sentiment_score"]].mean().reset_index()