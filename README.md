# AI-Based Network Traffic Behavior Analysis for Detecting Fake Users (Bots)

## 1. Project Overview

This project demonstrates how machine learning can classify
network traffic patterns as human-like or bot-like.

## 2. Problem Statement

Websites may receive automated requests from bots.
This project explores how traffic behavior features can help
classify these patterns using machine learning.

## 3. Algorithms Used

- Logistic Regression
- Decision Tree
- Random Forest

## 4. Features Used

- Requests per second
- Average time gap between requests
- Number of unique URLs
- Repeated request ratio
- Session duration

## 5. Evaluation Metrics

The models are compared using:

- Accuracy
- Precision
- Recall
- F1 Score

## 6. Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Google Colab
- GitHub

## 7. Project Files

- app.py: Streamlit website
- generate_dataset.py: Creates the sample dataset
- bot_traffic_dataset.csv: Synthetic dataset
- models/best_model.pkl: Trained machine learning model
- results/model_comparison.csv: Model evaluation results
- requirements.txt: Python dependencies

## 8. How to Run Locally

1. Install Python.
2. Install the packages using:

   pip install -r requirements.txt

3. Start the website using:

   streamlit run app.py

## 9. Dataset Disclaimer

The current dataset is synthetic and generated for educational
demonstration. The reported evaluation results do not establish
real-world bot detection performance.

## 10. Future Improvements

- Evaluate the models using a suitable real-world dataset.
- Improve the model using more representative traffic features.
- Test the website with additional examples.
