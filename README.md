# 🚀 SpamBuster - Spam Comment Detector

SpamBuster is a **machine learning-powered spam comment detector** built using **Streamlit**. It allows users to analyze comments for spam using different ML models, including Decision Tree, Logistic Regression, and K-Nearest Neighbors.

## 🎯 Features

👉 **Multiple ML Models** – Choose from Decision Tree, Logistic Regression, or KNN.\
👉 **Interactive UI** – Built with **Streamlit** for an intuitive and responsive interface.\
👉 **Real-time Spam Detection** – Instantly check whether a comment is spam or not.\
👉 **Custom Theming** – Light and dark theme support.\
👉 **Logo Branding** – Display your custom logo in the sidebar.

---

## 🛠️ Installation & Setup

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/Shahzeb-Mustafa/spambuster.git
cd spambuster
```

### **2️⃣ Install Dependencies**

Make sure you have **Python 3.8+** installed, then run:

```bash
pip install -r requirements.txt
```

### **3️⃣ Run the Application**

```bash
streamlit run app.py
```

---

## 🏠 Project Structure

```
📂 spambuster  
├── 📄 app.py              # Main Streamlit application  
├── 📄 requirements.txt    # Dependencies  
├── 📄 README.md           # Project documentation  
├── 📂 models              # Pre-trained ML models  
│   ├── spam1.pkl          # Decision Tree  
│   ├── linear.pkl         # Logistic Regression  
│   ├── knn.pkl           # KNN  
├── 📂 vectorizers         # TF-IDF Vectorizers  
│   ├── tfidf_vectorize1.pkl  
│   ├── linearvectorizor.pkl  
│   ├── knnvectorizor.pkl  
├── 📂 assets              # Static files (logo, images)  
│   ├── logo.png           # App Logo  
```

---

## 🖥️ Usage

1. **Select a Model** from the sidebar.
2. **Enter a comment** in the text box.
3. Click **"Check for Spam"** to get a prediction.
4. The app will display **🚨 Spam** or **✅ Not Spam**.

---

## ⚙️ Supported Models

| Model                            | Description                                    |
| -------------------------------- | ---------------------------------------------- |
| 🌳 **Decision Tree**             | A simple tree-based model for spam detection.  |
| 📈 **Logistic Regression**       | A linear model for binary classification.      |
| 🏠 **K-Nearest Neighbors (KNN)** | A distance-based algorithm for spam detection. |

---

## 🛠️ Tech Stack

- **Python** 🐍
- **Streamlit** 🎨 (For UI)
- **Scikit-learn** 🤖 (Machine Learning Models)
- **Joblib** 🛋️ (Model Loading)
- **NumPy & Pandas** 📊 (Data Processing)

---

## 🖼️ Screenshots



---

## 🤝 Contributing

1. **Fork** this repository.
2. **Clone** your fork.
3. Create a **new branch** for your changes.
4. Commit & push your changes.
5. Submit a **pull request**!

---

## 📝 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

## 🌟 Acknowledgments

Special thanks to **Streamlit**, **Scikit-learn**, and the **open-source community** for making this possible.

---

### 🚀 Happy Spam Busting! 🛡️

