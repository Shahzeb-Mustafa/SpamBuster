from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

# Load dataset
df = pd.read_csv(r"spam_database.csv")

# Define features and target
vectorizer = TfidfVectorizer()  # Convert text into numerical format
X = vectorizer.fit_transform(df['CONTENT'])  # Apply TF-IDF on the text column
y = df['CLASS']  # Target variable (spam or not)

# Split dataset
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Train model
dtc = DecisionTreeClassifier()
dtc.fit(x_train, y_train)

# Predict
y_pred = dtc.predict(x_test)

print("Model trained successfully!")
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
import joblib
joblib.dump(dtc, "spam1.pkl")
joblib.dump(vectorizer, "tfidf_vectorize1.pkl")
print("Model saved successfully!")