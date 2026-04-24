# 🧠 Mental Health & Digital Behavior Analysis

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

## 🚀 Future Work

- Deploy the saved Machine Learning model into a live, interactive web application using Streamlit to allow users to predict their anxiety levels in real-time.

---

## 🛠️ Tools Used

- **Python:** Pandas, NumPy

- **Machine Learning:** Scikit-Learn (Logistic Regression, Random Forest, StandardScaler)

- **Data Visualization:** Matplotlib, Seaborn