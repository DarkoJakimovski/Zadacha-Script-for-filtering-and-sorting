import json
from datetime import datetime


with open("reviews.json", "r") as f:
    reviews = json.load(f)


prioritize_text = True
minimum_rating = 3

"""Филтрирајте ги прегледите по минимален рејтинг"""
filtered_reviews = [review for review in reviews if review["rating"] >= minimum_rating]

"""Сортирај ги прегледите по текст"""
if prioritize_text:
    text_reviews = [review for review in filtered_reviews if "reviewText" in review and review["reviewText"] != ""]
    non_text_reviews = [review for review in filtered_reviews if "reviewText" not in review or review["reviewText"] == ""]
    text_reviews.sort(key=lambda review: (-review["rating"], datetime.fromisoformat(review["reviewCreatedOnDate"]),))
    non_text_reviews.sort(key=lambda review: (-review["rating"], datetime.fromisoformat(review["reviewCreatedOnDate"]),))
    filtered_reviews = text_reviews + non_text_reviews
else:
    filtered_reviews.sort(key=lambda review: (-review["rating"], datetime.fromisoformat(review["reviewCreatedOnDate"]),))

"""Напишете ги филтрираните и сортирани прегледи во датотека JSON"""
with open("filtered_reviews.json", "w") as f:
    json.dump(filtered_reviews, f, indent=4)

print("Filtered and sorted reviews written to filtered_reviews.json")


