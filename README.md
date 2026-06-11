# 📩 SMS Spam Classifier

## Overview

SMS Spam Classifier is a Machine Learning and Natural Language Processing (NLP) project that classifies SMS messages as **Spam** or **Ham (Not Spam)**. The model is trained using the SMS Spam Collection dataset and deployed through a Streamlit web application for real-time predictions.

---

## Features

* SMS Spam Detection
* Text Preprocessing using NLP
* TF-IDF Feature Extraction
* Multinomial Naive Bayes Classifier
* Interactive Streamlit Web Application
* Real-time Message Prediction
* Model Persistence using Pickle

---

## Dataset

The project uses the SMS Spam Collection Dataset containing 5,572 SMS messages labeled as:

* Ham (Legitimate Messages)
* Spam (Unwanted Promotional/Fraudulent Messages)

---

## Project Workflow

1. Data Collection
2. Data Cleaning
3. Text Preprocessing

   * Lowercase Conversion
   * Tokenization
   * Stopword Removal
   * Stemming
4. Feature Extraction using TF-IDF
5. Train-Test Split
6. Model Training using Multinomial Naive Bayes
7. Model Evaluation
8. Model Serialization using Pickle
9. Streamlit Deployment

---

## Technologies Used

* Python
* Pandas
* NumPy
* NLTK
* Scikit-learn
* Streamlit
* Pickle

---

## Project Structure

```text
SMS-Spam-Classifier/
│
├── app.py
├── spam_classifier.ipynb
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── spam.csv
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Pavani29105/SMS-Spam-Classifier/
cd SMS-Spam-Classifier
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Locally

```bash
streamlit run app.py
```

The application will open in your browser.

---

## Model Performance

* Algorithm: Multinomial Naive Bayes
* Feature Extraction: TF-IDF Vectorization
* Accuracy: High classification accuracy on the SMS Spam Collection dataset
* Evaluated using:

  * Accuracy Score
  * Precision Score
  * Confusion Matrix

---

## Example Predictions

### Spam

```text
Congratulations! You have won a free iPhone. Claim now!
```

Prediction:

```text
Spam
```

### Ham

```text
Hey, are we meeting at 5 PM today?
```

Prediction:

```text
Ham
```

---

## Future Improvements

* Logistic Regression
* Support Vector Machine (SVM)
* Random Forest
* Deep Learning Models (LSTM/BERT)
* Cloud Deployment
* Enhanced User Interface

---

## Author

Developed as a Machine Learning and NLP project to demonstrate text classification, feature engineering, and model deployment using Streamlit.
