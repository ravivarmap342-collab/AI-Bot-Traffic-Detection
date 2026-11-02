
import streamlit as st
import pandas as pd
import joblib
import os

# Page configuration
st.set_page_config(
    page_title="AI Bot Traffic Detector",
    page_icon="🤖",
    layout="wide"
)

# Load saved files
MODEL_PATH = "best_model.pkl"
DATA_PATH = "bot_traffic_dataset.csv"
RESULTS_PATH = "model_comparison.csv"

st.title("🤖 AI-Based Network Traffic Analyzer")
st.caption("Machine Learning Project | Human-like vs Bot-like Traffic")

# Check required files
if not os.path.exists(MODEL_PATH):
    st.error("Trained model not found. Please train the model first.")
    st.stop()

if not os.path.exists(DATA_PATH):
    st.error("Dataset not found. Please generate the dataset first.")
    st.stop()

model = joblib.load(MODEL_PATH)
data = pd.read_csv(DATA_PATH)

# Sidebar navigation
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Choose a page",
    [
        "Dashboard",
        "Analyze Traffic",
        "Dataset Explorer",
        "Model Comparison",
        "About Project"
    ]
)

# Dashboard
if page == "Dashboard":

    st.header("Project Dashboard")

    st.write(
        "This project uses machine learning to classify "
        "network traffic as human-like or bot-like."
    )

    total_records = len(data)
    human_records = int((data["label"] == 0).sum())
    bot_records = int((data["label"] == 1).sum())

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Records", total_records)
    col2.metric("Human-like Records", human_records)
    col3.metric("Bot-like Records", bot_records)

    st.subheader("Traffic Distribution")

    chart_data = pd.DataFrame({
        "Traffic Type": ["Human-like", "Bot-like"],
        "Number of Records": [human_records, bot_records]
    })

    st.bar_chart(
        chart_data.set_index("Traffic Type")
    )

    st.info(
        "Educational demo: the current dataset is synthetic, "
        "not collected from real network users."
    )

# Analyze Traffic
elif page == "Analyze Traffic":

    st.header("🔍 Analyze Network Traffic")

    st.write(
        "Enter traffic information and let the trained "
        "machine learning model classify the example."
    )

    with st.form("traffic_form"):

        requests = st.number_input(
            "Requests per second",
            min_value=0.0,
            max_value=1000.0,
            value=3.0
        )

        gap = st.number_input(
            "Average time gap between requests (milliseconds)",
            min_value=0.0,
            max_value=100000.0,
            value=1000.0
        )

        urls = st.number_input(
            "Number of unique URLs",
            min_value=0,
            max_value=10000,
            value=10
        )

        repeated = st.slider(
            "Repeated request ratio",
            min_value=0.0,
            max_value=1.0,
            value=0.2
        )

        duration = st.number_input(
            "Session duration (seconds)",
            min_value=0.0,
            max_value=100000.0,
            value=120.0
        )

        submitted = st.form_submit_button(
            "Analyze Traffic"
        )

    if submitted:

        input_data = pd.DataFrame([{
            "requests_per_second": requests,
            "avg_time_gap_ms": gap,
            "unique_urls": urls,
            "repeated_request_ratio": repeated,
            "session_duration_sec": duration
        }])

        prediction = int(model.predict(input_data)[0])

        if prediction == 1:
            st.error("Prediction: Bot-like Traffic 🤖")
        else:
            st.success("Prediction: Human-like Traffic 👤")

        st.caption(
            "This is a model prediction, not proof of a user's identity. "
            "The model was trained on synthetic example data."
        )

# Dataset Explorer
elif page == "Dataset Explorer":

    st.header("📁 Dataset Explorer")

    st.write("Preview of the sample traffic dataset.")

    st.dataframe(data.head(50), use_container_width=True)

    st.subheader("Dataset Information")

    col1, col2 = st.columns(2)

    col1.metric("Rows", data.shape[0])
    col2.metric("Columns", data.shape[1])

    st.write("Label meanings:")
    st.write("- 0 = Human-like traffic")
    st.write("- 1 = Bot-like traffic")

    st.download_button(
        label="Download Dataset CSV",
        data=data.to_csv(index=False).encode("utf-8"),
        file_name="bot_traffic_dataset.csv",
        mime="text/csv"
    )

# Model Comparison
elif page == "Model Comparison":

    st.header("📊 Machine Learning Model Comparison")

    if os.path.exists(RESULTS_PATH):

        results = pd.read_csv(RESULTS_PATH)

        st.dataframe(
            results,
            use_container_width=True,
            hide_index=True
        )

        st.subheader("F1 Score Comparison")

        if "F1 Score (%)" in results.columns:

            chart = results.set_index("Algorithm")[
                ["F1 Score (%)"]
            ]

            st.bar_chart(chart)

        st.info(
            "These results come from a synthetic dataset. "
            "Real-world performance may be different."
        )

    else:
        st.warning(
            "Model comparison results were not found."
        )

# About Project
elif page == "About Project":

    st.header("ℹ️ About This Project")

    st.write("""
    **Project Title:**

    AI-Based Network Traffic Behavior Analysis for Detecting Fake Users (Bots)

    **Problem Statement:**

    Automated bots can generate repeated or unusually frequent
    requests to websites. This project demonstrates how machine
    learning can classify traffic patterns.

    **Algorithms Used:**

    - Logistic Regression
    - Decision Tree
    - Random Forest

    **Evaluation Metrics:**

    - Accuracy
    - Precision
    - Recall
    - F1 Score

    **Technology Used:**

    - Python
    - Pandas
    - Scikit-learn
    - Streamlit
    - Google Colab
    - GitHub

    **Important Limitation:**

    The current dataset contains artificially generated examples.
    This is an educational prototype, not a validated real-world
    bot detection system.
    """)

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("AI & ML Mini Project")
st.sidebar.caption("Educational Demonstration")
