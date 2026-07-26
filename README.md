# AI Review Sentiment Dataset (45K+ Multi-Domain Reviews)

A high-quality synthetic dataset containing **45,647 customer reviews** across **15 product and service domains**. The dataset is designed for **Sentiment Analysis**, **Natural Language Processing (NLP)**, **Text Classification**, **Machine Learning**, and **Deep Learning** applications.

---

## Overview

This repository provides a realistic multi-domain review dataset enriched with sentiment labels and contextual metadata. Each review includes user information, review metadata, product details, ratings, emotions, recommendation scores, and company responses, making it suitable for a wide range of AI and NLP tasks.

The dataset was created to help students, researchers, and developers build and evaluate sentiment analysis models without relying on proprietary customer data.

---

## Dataset Statistics

| Feature | Value |
|---------|------:|
| Total Reviews | 45,647 |
| Total Features | 23 |
| Categories | 15 |
| Sentiment Classes | 3 |
| Languages | English |
| Duplicate Reviews | 0 |
| Missing Values | 0 |

---

## Categories

- Electronics
- Mobile Phones
- Laptops
- Restaurants
- Hotels
- Books
- Movies
- Gaming
- Software
- Grocery
- Banking
- Healthcare
- Education
- Airlines
- Clothing

---

## Dataset Features

| Column | Description |
|---------|-------------|
| review_id | Unique review identifier |
| user_id | Unique user identifier |
| username | Randomly generated username |
| review_title | Review headline |
| review | Customer review text |
| sentiment | Positive, Negative, Neutral |
| category | Product or service category |
| product | Product or service name |
| rating | Rating (1–5) |
| verified_purchase | Purchase verification status |
| helpful_votes | Number of helpful votes |
| review_length | Number of words in the review |
| purchase_date | Purchase date |
| review_date | Review publication date |
| country | Country of reviewer |
| language | Review language |
| source | Review platform |
| device | Mobile, Desktop, or Tablet |
| review_type | Short, Medium, or Long review |
| writing_style | Formal, Casual, Enthusiastic, Critical |
| emotion | Predicted emotional tone |
| recommendation_score | Recommendation score (1–10) |
| company_response | Example company response |

---

## Repository Structure

```
AI-Review-Sentiment-Dataset/
│
├── reviews_dataset.csv
├── reviews_dataset.xlsx
├── data_dictionary.csv
├── LICENSE
├── README.md
├── data/
├── scripts/
└── notebooks/
```

---

## Applications

This dataset can be used for:

- Sentiment Analysis
- Text Classification
- Opinion Mining
- Machine Learning
- Deep Learning
- Transformer Models (BERT, RoBERTa, DistilBERT)
- Large Language Model (LLM) Fine-Tuning
- Emotion Detection
- Recommendation Systems
- Customer Feedback Analysis
- Educational Projects
- Data Visualization
- Research and Benchmarking

---

## Data Quality

The dataset has been validated to ensure high quality.

- No missing values
- No duplicate reviews
- Balanced category distribution
- Rich contextual metadata
- Multiple writing styles
- Realistic review lengths
- Context-aware review generation
- Consistent sentiment labels

---

## File Formats

The dataset is available in multiple formats.

- CSV
- JSON
- XLSX

---

## Getting Started

Clone the repository:

```bash
git clone https://github.com/your-username/AI-Review-Sentiment-Dataset.git
```

Install dependencies:

```bash
pip install pandas openpyxl faker tqdm
```

Load the dataset:

```python
import pandas as pd

df = pd.read_csv("reviews_dataset.csv")

print(df.head())
```

---

## Example Use Cases

- Build a sentiment classification model
- Train transformer-based NLP models
- Perform exploratory data analysis
- Visualize customer feedback trends
- Benchmark machine learning algorithms
- Develop recommendation systems
- Conduct NLP research

---

## License

This project is licensed under the **CC BY 4.0 License**. See the `LICENSE` file for more information.

---

## Author

**Mobeen Fatima**

BS Computer Science Student (Specialized AI)

### Connect with Me

- **GitHub:** https://github.com/mobeenfatimaa
- **Kaggle:** https://www.kaggle.com/mobeenfatimah
- **LinkedIn:** https://www.linkedin.com/in/mobeen-fatima-599a35347/

---

## Contributing

Contributions, suggestions, and improvements are welcome. Feel free to open an issue or submit a pull request.

---

## Acknowledgments

This dataset was created as part of an AI and NLP initiative to provide an open, realistic, and reusable benchmark dataset for the machine learning community.

If you find this repository useful, consider giving it a ⭐ to support future open-source AI and NLP projects.
