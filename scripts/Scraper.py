from google_play_scraper import Sort, reviews
import csv
import os
from datetime import datetime

# Define Play Store ID for the app
bank_playstore_id = "com.dashen.dashensuperapp"

# Fetch reviews
result, continuation_token = reviews(
    bank_playstore_id,
    lang="en",
    country="us",
    sort=Sort.NEWEST,
    count=600,
    filter_score_with=None,
)

# Define your desired path
save_dir = "/home/samrawit/Desktop/Banking_Application_Experience_Analysis/Data/raw"

# Ensure the directory exists
os.makedirs(save_dir, exist_ok=True)

# Create a timestamped filename
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
csv_filename = os.path.join(save_dir, f"Dashen_reviews_{timestamp}.csv")

# Define CSV header
fieldnames = [
    "User Name", "Rating", "Date", "Review Content", "Review ID", "App Version",
    "Replied At", "Reply Content", "Thumbs Up Count", "User Image URL"
]

# Write reviews to CSV
with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for review in result:
        writer.writerow({
            "User Name": review.get("userName", ""),
            "Rating": review.get("score", ""),
            "Date": review.get("at").strftime('%Y-%m-%d %H:%M:%S') if review.get("at") else "N/A",
            "Review Content": review.get("content", ""),
            "Review ID": review.get("reviewId", ""),
            "App Version": review.get("appVersion", ""),
            "Replied At": review.get("repliedAt", "—"),
            "Reply Content": review.get("replyContent", "—"),
            "Thumbs Up Count": review.get("thumbsUpCount", ""),
            "User Image URL": review.get("userImage", "")
        })

print(f"✅ Successfully saved 100 reviews to {csv_filename}")
