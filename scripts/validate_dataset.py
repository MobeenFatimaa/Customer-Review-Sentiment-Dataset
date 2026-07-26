import pandas as pd

# ===========================
# Load Dataset
# ===========================
df = pd.read_csv("../reviews_dataset.csv")

print("=" * 70)
print("        AI REVIEW SENTIMENT DATASET VALIDATION REPORT")
print("=" * 70)

# ===========================
# Basic Information
# ===========================
print("\nDATASET OVERVIEW")
print("-" * 70)

print(f"Total Rows      : {len(df):,}")
print(f"Total Columns   : {len(df.columns)}")

print("\nColumn Names:")
for col in df.columns:
    print(f" - {col}")

# ===========================
# Missing Values
# ===========================
print("\n" + "=" * 70)
print("MISSING VALUES")
print("=" * 70)

missing = df.isnull().sum()

if missing.sum() == 0:
    print("No missing values found.")
else:
    print(missing)

# ===========================
# Duplicate Reviews
# ===========================
print("\n" + "=" * 70)
print("DUPLICATE CHECK")
print("=" * 70)

duplicates = df.duplicated(subset=["review"]).sum()

print(f"Duplicate Reviews : {duplicates:,}")

# ===========================
# Sentiment Distribution
# ===========================
print("\n" + "=" * 70)
print("SENTIMENT DISTRIBUTION")
print("=" * 70)

sentiments = df["sentiment"].value_counts()

for s, c in sentiments.items():
    print(f"{s:<12}: {c:,}")

# ===========================
# Rating Distribution
# ===========================
print("\n" + "=" * 70)
print("RATING DISTRIBUTION")
print("=" * 70)

ratings = df["rating"].value_counts().sort_index()

for r, c in ratings.items():
    print(f"{r} Stars : {c:,}")

# ===========================
# Category Distribution
# ===========================
print("\n" + "=" * 70)
print("CATEGORY DISTRIBUTION")
print("=" * 70)

cats = df["category"].value_counts()

for cat, c in cats.items():
    print(f"{cat:<20}: {c:,}")

# ===========================
# Verified Purchase
# ===========================
print("\n" + "=" * 70)
print("VERIFIED PURCHASE")
print("=" * 70)

verified = df["verified_purchase"].value_counts()

for v, c in verified.items():
    print(f"{v:<5}: {c:,}")

# ===========================
# Device Distribution
# ===========================
print("\n" + "=" * 70)
print("DEVICE DISTRIBUTION")
print("=" * 70)

devices = df["device"].value_counts()

for d, c in devices.items():
    print(f"{d:<10}: {c:,}")

# ===========================
# Writing Style
# ===========================
print("\n" + "=" * 70)
print("WRITING STYLE")
print("=" * 70)

styles = df["writing_style"].value_counts()

for s, c in styles.items():
    print(f"{s:<15}: {c:,}")

# ===========================
# Emotion Distribution
# ===========================
print("\n" + "=" * 70)
print("EMOTION DISTRIBUTION")
print("=" * 70)

emotion = df["emotion"].value_counts()

for e, c in emotion.items():
    print(f"{e:<10}: {c:,}")

# ===========================
# Countries
# ===========================
print("\n" + "=" * 70)
print("COUNTRIES")
print("=" * 70)

countries = df["country"].value_counts()

for country, c in countries.items():
    print(f"{country:<15}: {c:,}")

# ===========================
# Review Length
# ===========================
print("\n" + "=" * 70)
print("REVIEW LENGTH")
print("=" * 70)

print(f"Minimum Words : {df['review_length'].min()}")
print(f"Maximum Words : {df['review_length'].max()}")
print(f"Average Words : {round(df['review_length'].mean(),2)}")

# ===========================
# Helpful Votes
# ===========================
print("\n" + "=" * 70)
print("HELPFUL VOTES")
print("=" * 70)

print(f"Minimum : {df['helpful_votes'].min()}")
print(f"Maximum : {df['helpful_votes'].max()}")
print(f"Average : {round(df['helpful_votes'].mean(),2)}")

# ===========================
# Dataset Memory Usage
# ===========================
print("\n" + "=" * 70)
print("MEMORY USAGE")
print("=" * 70)

memory = df.memory_usage(deep=True).sum() / 1024 / 1024

print(f"{memory:.2f} MB")

# ===========================
# Save Validation Report
# ===========================
report = {
    "Total Rows": len(df),
    "Total Columns": len(df.columns),
    "Duplicate Reviews": duplicates,
    "Missing Values": int(missing.sum()),
    "Average Review Length": round(df["review_length"].mean(), 2),
    "Average Helpful Votes": round(df["helpful_votes"].mean(), 2)
}

pd.DataFrame(report.items(), columns=["Metric", "Value"]).to_csv(
    "../validation_report.csv",
    index=False
)

print("\n" + "=" * 70)
print("VALIDATION COMPLETED SUCCESSFULLY")
print("=" * 70)

print("\nValidation report saved as:")
print("validation_report.csv")