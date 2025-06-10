import pandas as pd
import re
from typing import Dict, List
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from collections import Counter

def map_rating_to_sentiment(rating):
    if rating >= 4:
        return 'positive'
    elif rating <= 2:
        return 'negative'
    else:
        return 'neutral'

def get_top_words(texts, n=5):
    words = []
    for text in texts:
        tokens = re.findall(r'\b[a-z]{3,}\b', str(text).lower())
        words.extend([w for w in tokens if w not in ENGLISH_STOP_WORDS])
    return [w for w, _ in Counter(words).most_common(n)]

def identify_drivers_and_pain_points(
    df,
    sentiment_col='sentiment_label',  
    text_col='Review',
    bank_col='Bank'
):
    insights = {}
    for bank in df[bank_col].unique():
        bank_df = df[df[bank_col] == bank]
        pos_texts = bank_df[bank_df[sentiment_col] == 'positive'][text_col]
        neg_texts = bank_df[bank_df[sentiment_col] == 'negative'][text_col]
        insights[bank] = {
            'drivers': get_top_words(pos_texts),
            'painpoints': get_top_words(neg_texts)
        }
    return insights

def compare_banks(df: pd.DataFrame, bank_col: str = 'Bank', sentiment_col: str = 'sentiment_label') -> pd.DataFrame:
    
    return df.groupby([bank_col, sentiment_col]).size().unstack(fill_value=0)

def suggest_improvements() -> List[str]:
    
    return [
        
    ]

