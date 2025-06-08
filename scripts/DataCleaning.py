import pandas as pd
import re

class DataCleaner:
    def __init__(self, dataframe):
        self.df = dataframe
    
    def convert_to_lowercase(self):
        """Convert all text in 'Review Content' to lowercase."""
        self.df['Review Content'] = self.df['Review Content'].str.lower()

    def remove_duplicates(self):
        """Remove duplicate rows based on 'Review Content'."""
        duplicates = self.df[self.df.duplicated(subset=['Review Content'], keep=False)]
        print("Duplicates found:")
        print(duplicates)
        self.df = self.df.drop_duplicates(subset=['Review Content'], keep='first')
    
    def remove_nulls(self):
        """Check for null values in 'Review Content'."""
        nulls = self.df['Review Content'].isnull().any()
        if nulls:
            print("Null values found in 'Review Content'.")
    
    def filter_ethiopian_chars(self):
        """Remove rows containing Ethiopian characters."""
        self.df = self.df[~self.df['Review Content'].str.contains(r'[\u1200-\u137F]', na=False)]
    
    def remove_emojis(self):
        """Remove emojis from 'Review Content'."""
        emoji_pattern = re.compile(
            "[" 
            "\U0001F600-\U0001F64F"  # emoticons
            "\U0001F300-\U0001F5FF"  # symbols & pictographs
            "\U0001F680-\U0001F6FF"  # transport & map symbols
            "\U0001F1E0-\U0001F1FF"  # flags
            "\U00002702-\U000027B0"  # dingbats
            "\U000024C2-\U0001F251"  
            "]+", flags=re.UNICODE
        )
        self.df['Review Content'] = self.df['Review Content'].apply(
            lambda x: emoji_pattern.sub(r'', x) if isinstance(x, str) else x
        )
    
    def get_cleaned_data(self):
        """Return the cleaned DataFrame."""
        return self.df


import sys
print(sys.path)
 
# Usage example (to be run outside this module):
# df = pd.read_csv('your_data.csv')  # Load your DataFrame
# cleaner = DataCleaner(df)
# cleaner.remove_duplicates()
# cleaner.remove_nulls()
# cleaner.filter_ethiopian_chars()
# cleaner.remove_emojis()
# cleaned_df = cleaner.get_cleaned_data()