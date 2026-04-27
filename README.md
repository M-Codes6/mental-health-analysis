# 🧠 Mental Health & Digital Behavior Analysis

## 🚀 Live Web Application: Digital Anxiety Predictor

As the culmination of this project, the trained Random Forest model is deployed into a live, interactive web application using **Streamlit**. 

The app translates complex Machine Learning predictions into a user-friendly interface. It captures real-time user inputs (Digital Wellbeing Score, Screen Time, Mood, etc.), scales the data dynamically to match the training distribution, and instantly predicts the user's anxiety level (Low, Medium, High).

**[🔗 Click Here to View the Live App]**(Add_Your_Streamlit_Link_Here_Soon)

---

## 📌 Project Overview

This project analyzes how digital behavior (screen time, social media usage, notifications, and sleep) impacts mental health indicators. 

The goal was to move from assumptions to data-driven insights using Exploratory Data Analysis (EDA), and then build a Machine Learning pipeline to predict user anxiety and extract actionable business recommendations.

---

## 📊 Dataset

- 500 rows, 9 numerical features
- No missing values
- Features include: Screen time, Sleep hours, Notification count, Social media usage, Digital Wellbeing Score, and Anxiety levels.

---

## 🔍 Steps Performed

### 1. Data Understanding & EDA
- Checked structure, data types, and statistics.
- Analyzed distributions of screen time, sleep hours, notifications, and anxiety levels.
- Explored relationships using scatter plots and correlation heatmaps.

### 2. Baseline Machine Learning
- Split data into 80/20 Train/Test sets.
- Applied `StandardScaler` to normalize feature weights.
- Trained a baseline Logistic Regression model, which achieved 74% accuracy.

### 3. Diagnosing Bias & Target Engineering
- Deployed a Confusion Matrix and discovered the "Accuracy Trap" (the model was highly biased toward the majority class due to data imbalance).
- Engineered the target variable (`anxiety_level`) into three broad categories (Low, Medium, High) using `pd.cut()` to group the data and simplify the decision boundary.

### 4. Advanced Modeling & Feature Importance
- Retrained models on the engineered target, boosting Logistic Regression accuracy to 99% and Random Forest to 90%.
- Extracted Feature Importance from the Random Forest to identify the exact behaviors driving user anxiety.

### 5. Model Deployment
- Saved the trained model and scaler as `.pkl` files using `joblib`.
- Built a frontend UI with Streamlit to capture user habits via interactive sliders.
- Handled live data preprocessing (scaling) to ensure user inputs matched the model's exact training environment.

---

## 📌 Key Insights

- **The "Digital Wellbeing" Factor:** Feature Importance revealed that a user's overall "Digital Wellbeing Score" makes up over 50% of the model's decision-making power, vastly outweighing raw screen time.
- **Quality over Quantity:** Social media usage has a much stronger relationship with anxiety than overall screen time. It is about *how* time is spent, not just *how much*.
- **The Accuracy Trap:** Predicting complex psychological scales (1-10) on imbalanced data leads to biased models. Grouping data into broader actionable categories (Low/Medium/High) drastically improves model reliability.

---

## 💡 Recommendations

- **App Developers:** Instead of just tracking raw screen time, implement holistic "Digital Wellbeing" metrics (tracking late-night usage, focus modes, etc.) to better predict and prevent user burnout.
- **Users:** Focus on actively managing social media consumption and notifications, rather than just trying to reduce overall screen time.

---



## 🛠️ Technical Implementation & Challenges Overcome

Deploying this model from a static Jupyter Notebook to a live web application required solving several real-world engineering and data translation challenges:

* **Strict Data Pipeline Formatting:** Engineered the Streamlit backend to capture raw slider inputs and pack them into a Pandas DataFrame that perfectly mirrored the original `X_train` dataset. This prevented critical shape mismatch and column-order errors during live predictions.
* **Dynamic On-the-Fly Preprocessing:** Loaded the saved `StandardScaler` (`.pkl`) into the app environment to dynamically scale live user inputs, ensuring the model evaluated the exact same statistical distribution it was trained on.
* **Resolving Scale Logic Bugs:** Debugged a critical real-world UI-to-Model translation bug where default slider boundaries (e.g., a 0-10 scale) conflicted with the actual dataset distribution (e.g., a 34-80 scale). Adjusted the frontend constraints to strictly enforce the model's expected reality, preventing false "High Anxiety" baseline predictions.



---

## 💻 How to Run the App Locally

If you want to run this application on your own machine to test the model:


**1. Clone this repository**
```bash
git clone [https://github.com/YourUsername/Mental-Health-and-Digital-Behavior.git](https://github.com/M-Codes6/mental-health-analysis.git)
cd Mental-Health-and-Digital-Behavior



**2. Install the required dependencies**
   -----   pip install -r requirements.txt    --------


**3. Launch the Streamlit server**

  -----    Streamlit run app.py    -----



## 🛠️ Tools Used

- **Python:** Pandas, NumPy

- **Machine Learning:** Scikit-Learn (Logistic Regression, Random Forest, StandardScaler), Joblib

- **Web Deployment:** Streamlit

- **Data Visualization:** Matplotlib, Seaborn