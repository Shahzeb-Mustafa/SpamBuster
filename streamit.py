import streamlit as st
import joblib
import numpy as np

# Logo path
logo_path = "spambuster.png"  # Change this to your logo file path

# Load models
try:
    dtc = joblib.load("spam1.pkl")  # Decision Tree
    log_reg = joblib.load("linear.pkl")  # Logistic Regression
    knn = joblib.load("knn.pkl")  # KNN
except Exception as e:
    st.error(f"Error loading models: {e}")
    st.stop()

# Streamlit UI - Sidebar
st.sidebar.image(logo_path, width=230, use_container_width=True)
# Adjust width if needed
st.sidebar.title("⚙️ Algorithms")
model_option = st.sidebar.radio("Choose a model:",
                                ("Decision Tree 🌳", "Logistic Regression 📈", "K-Nearest Neighbors 🏠"))
theme = st.sidebar.selectbox("Select Theme:", ["Light", "Dark"])

# Load the correct vectorizer based on model choice
vectorizer_path = {
    "Decision Tree 🌳": "tfidf_vectorize1.pkl",
    "Logistic Regression 📈": "linearvectorizor.pkl",
    "K-Nearest Neighbors 🏠": "knnvectorizor.pkl"
}

try:
    vectorizer = joblib.load(vectorizer_path[model_option])
    if not hasattr(vectorizer, "transform"):
        st.error(f"Vectorizer for {model_option} is not valid.")
        st.stop()
except Exception as e:
    st.error(f"Error loading vectorizer for {model_option}: {e}")
    st.stop()

# Text input
st.title("SpamBuster")
st.write("SpamBuster – Eliminate spam, keep comments clean! 🛡️")
new_comment = st.text_area("Enter a comment:", key="input_text")

# Button to check spam
if st.button("Check for Spam"):
    if new_comment.strip():
        try:
            new_comment_tfidf = vectorizer.transform([new_comment])

            # Select model
            model = {
                "Decision Tree 🌳": dtc,
                "Logistic Regression 📈": log_reg,
                "K-Nearest Neighbors 🏠": knn
            }[model_option]

            prediction = model.predict(new_comment_tfidf)[0]
            result = "🚨 Spam" if prediction == 1 else "✅ Not Spam"
            st.subheader(f"Prediction: {result}")
        except Exception as e:
            st.error(f"Error processing input: {e}")
    else:
        st.warning("Please enter a comment to check.")
