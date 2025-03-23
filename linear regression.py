from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv(r"spam_database.csv")

# Define features and target
vectorizer = TfidfVectorizer()  # Convert text into numerical format
X = vectorizer.fit_transform(df['CONTENT'])  # Apply TF-IDF on the text column
y = df['CLASS']  # Target variable (spam or not)

# Split dataset
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Train model using Logistic Regression
model = LogisticRegression()
model.fit(x_train, y_train)

# Predict
y_pred = model.predict(x_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Save model and vectorizer
joblib.dump(model, "linear.pkl")
joblib.dump(vectorizer, "linearvectorizor.pkl")
print("Model saved successfully!")
