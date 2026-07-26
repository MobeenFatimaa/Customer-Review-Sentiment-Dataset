import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../output/review_sentiment_dataset.csv")

plt.figure(figsize=(6,4))
df["sentiment"].value_counts().plot(kind="bar")
plt.title("Sentiment Distribution")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,4))
df["category"].value_counts().plot(kind="bar")
plt.title("Category Distribution")
plt.tight_layout()
plt.show()

plt.figure(figsize=(6,4))
df["rating"].hist(bins=5)
plt.title("Ratings")
plt.tight_layout()
plt.show()