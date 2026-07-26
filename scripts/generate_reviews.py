import json
import random
import pandas as pd
from faker import Faker
from tqdm import tqdm

fake = Faker()


# Helper function to load JSON files
def load_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


# Base Data
categories = load_json("../data/categories.json")
products = load_json("../data/products.json")

positive = load_json("../data/positive_phrases.json")
negative = load_json("../data/negative_phrases.json")
neutral = load_json("../data/neutral_phrases.json")

positive_adjectives = load_json("../data/positive_adjectives.json")
negative_adjectives = load_json("../data/negative_adjectives.json")
neutral_adjectives = load_json("../data/neutral_adjectives.json")

problems = load_json("../data/problems.json")
recommendations = load_json("../data/recommendations.json")

# Category-aware & Structural Data
category_templates = load_json("../data/category_templates.json")
aspects = load_json("../data/aspects.json")
transitions = load_json("../data/transitions.json")
opening_phrases = load_json("../data/opening_phrases.json")
closing_phrases = load_json("../data/closing_phrases.json")
time_phrases = load_json("../data/time_phrases.json")
intensifiers = load_json("../data/intensifiers.json")

# User & Metadata JSONs
users = load_json("../data/users.json")
review_titles = load_json("../data/review_titles.json")
company_responses = load_json("../data/company_responses.json")

# Style, Emoji & Typo JSONs
styles = load_json("../data/writing_styles.json")
emojis = load_json("../data/emojis.json")
typos = load_json("../data/typos.json")

# Target Dataset Size
NUM_REVIEWS = 50000

# Helper Lists
countries = [
    "USA",
    "Canada",
    "UK",
    "Germany",
    "France",
    "India",
    "Pakistan",
    "Australia",
    "Japan",
    "Brazil",
]

# Category-Aware Sources
sources = {
    "Electronics": ["Amazon", "Best Buy", "Newegg"],
    "Mobile Phones": ["Amazon", "Samsung Store", "Apple Store"],
    "Laptops": ["Amazon", "Dell Store", "HP Store", "Lenovo Store"],
    "Restaurants": ["Google Reviews", "Yelp", "TripAdvisor"],
    "Hotels": ["Booking.com", "Hotels.com", "TripAdvisor"],
    "Movies": ["IMDb", "Rotten Tomatoes"],
    "Books": ["Goodreads", "Amazon"],
    "Gaming": ["Steam", "Epic Games", "Metacritic"],
    "Software": ["G2", "Capterra", "Product Hunt"],
    "Healthcare": ["Google Reviews", "Healthgrades"],
    "Banking": ["Trustpilot", "Google Reviews"],
    "Education": ["Coursera", "Udemy", "Google Reviews"],
    "Grocery": ["Amazon Fresh", "Walmart", "Instacart"],
    "Airlines": ["Skytrax", "TripAdvisor"],
    "Clothing": ["Amazon", "Zara", "H&M"],
}


# Typing Mistakes Helper
def introduce_typos(text):
    if random.random() > 0.15:
        return text

    for correct, wrong in typos.items():
        if correct in text.lower():
            text = text.replace(correct, wrong)
            break

    return text


# Main Generator Function
def generate_review(review_number):
    # Balance Sentiments (40% Pos, 30% Neg, 30% Neu)
    sentiments = (
        ["Positive"] * 40 +
        ["Negative"] * 30 +
        ["Neutral"] * 30
    )
    sentiment = random.choice(sentiments)

    category = random.choice(categories)
    product = random.choice(products[category])
    aspect = random.choice(aspects[category])
    problem = random.choice(problems)
    transition = random.choice(transitions)
    time_phrase = random.choice(time_phrases)

    # Writing Style & Openings
    style = random.choice(list(styles.keys()))
    style_opening = random.choice(styles[style])

    standard_opening = random.choice(opening_phrases).format(
        product=product, time=time_phrase
    )

    # Select Sentiment Adjectives & Recommendations
    if sentiment == "Positive":
        adjective = random.choice(positive_adjectives)
        recommendation = random.choice(recommendations["Positive"])
    elif sentiment == "Negative":
        adjective = random.choice(negative_adjectives)
        recommendation = random.choice(recommendations["Negative"])
    else:
        adjective = random.choice(neutral_adjectives)
        recommendation = random.choice(recommendations["Neutral"])

    # Natural Rating Selection
    if sentiment == "Positive":
        rating = random.choice([4, 5, 5, 5])
    elif sentiment == "Neutral":
        rating = random.choice([3, 3, 2, 4])
    else:
        rating = random.choice([1, 1, 2, 2])

    # Category-Aware Templates
    template = random.choice(category_templates[category][sentiment])

    body = template.format(
        product=product,
        adjective=adjective,
        aspect=aspect,
        problem=problem,
        recommendation=recommendation,
    )

    closing = random.choice(closing_phrases)

    # Review Length Variety
    review_type = random.choice(["short", "medium", "long"])

    if review_type == "short":
        review = body
    elif review_type == "medium":
        review = f"{standard_opening} {body}"
    else:
        review = f"{style_opening} {standard_opening} {transition} {body} {closing}"

    # Mixed Sentiment Edge Cases
    if sentiment == "Positive" and random.random() < 0.05:
        review += " However, there are a few minor issues."
    if sentiment == "Negative" and random.random() < 0.05:
        review += " Still, it has a few good points."

    # Exclamation Marks
    if sentiment == "Positive" and random.random() < 0.08:
        review = review.replace(".", "!!", 1)

    # Emojis
    if random.random() < 0.30:
        emoji = " " + random.choice(emojis[sentiment])
        review += emoji

    # Apply Typos
    review = introduce_typos(review)

    # User Metadata
    first = random.choice(users["first_names"])
    last = random.choice(users["last_names"])
    username = f"{first.lower()}_{last.lower()}{random.randint(10, 999)}"
    user_id = f"USR{random.randint(100000, 999999)}"

    # Date Calculations
    purchase_date = fake.date_between(start_date="-5y", end_date="-10d")
    review_date = fake.date_between(start_date=purchase_date, end_date="today")

    title = random.choice(review_titles[sentiment])
    company_reply = random.choice(company_responses[sentiment])

    return {
        "review_id": f"REV{review_number:06}",
        "user_id": user_id,
        "username": username,
        "review_title": title,
        "review": review,
        "sentiment": sentiment,
        "category": category,
        "product": product,
        "rating": rating,
        "verified_purchase": random.choice(["Yes", "No"]),
        "helpful_votes": random.randint(0, 500),
        "review_length": len(review.split()),
        "purchase_date": purchase_date,
        "review_date": review_date,
        "country": random.choice(countries),
        "language": "English",
        "source": random.choice(sources[category]),
        "device": random.choice(["Mobile", "Desktop", "Tablet"]),
        "review_type": review_type.title(),
        "writing_style": style,
        "emotion": {
            "Positive": "Joy",
            "Negative": "Anger",
            "Neutral": "Neutral",
        }[sentiment],
        "recommendation_score": {
            "Positive": random.randint(8, 10),
            "Neutral": random.randint(5, 7),
            "Negative": random.randint(1, 4),
        }[sentiment],
        "company_response": company_reply,
    }


# Generate Large Dataset
dataset = []
for i in tqdm(range(NUM_REVIEWS)):
    dataset.append(generate_review(i + 1))

df = pd.DataFrame(dataset)

# Remove Duplicate Reviews Automatically
df = df.drop_duplicates(subset=["review"])

# Export Files to Root Directory
df.to_csv("../reviews_dataset.csv", index=False)

df.to_json(
    "../reviews_dataset.json",
    orient="records",
    indent=4
)

df.to_excel(
    "../reviews_dataset.xlsx",
    index=False
)
    
print(f"Final Dataset Shape: {df.shape}")
print("Dataset saved successfully to the root directory in CSV, JSON, and XLSX formats!")