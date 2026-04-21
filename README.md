# 🧠 Mental Health & Digital Behavior Analysis

## 📌 Project Overview
This project analyzes how digital behavior (screen time, social media usage, notifications, and sleep) impacts mental health indicators such as anxiety, focus, and mood.

The goal is to move from assumptions to data-driven insights using Exploratory Data Analysis (EDA) and correlation.

---

## 📊 Dataset
- 500 rows, 9 numerical features
- No missing values
- Includes:
  - Screen time
  - Sleep hours
  - Notification count
  - Social media usage
  - Focus, mood, and anxiety scores

---

## 🔍 Steps Performed

### 1. Data Understanding
- Checked structure, data types, and statistics
- Verified no missing values

### 2. Univariate Analysis
- Analyzed distributions of:
  - Screen time
  - Sleep hours
  - Notifications
  - Anxiety levels

### 3. Relationship Analysis
- Explored relationships using scatter plots:
  - Screen Time vs Anxiety
  - Sleep vs Anxiety
  - Notifications vs Focus

### 4. Correlation Analysis
- Used correlation matrix and heatmap
- Identified strongest and weakest relationships

---

## 📌 Key Insights
- Social media usage has a stronger relationship with anxiety than overall screen time
- Screen time and sleep do not significantly affect anxiety in this dataset
- Notifications negatively impact focus
- Human behavior is influenced by multiple factors, not a single variable

---

## 💡 Recommendations
- Reduce excessive social media usage
- Manage notifications to improve focus
- Focus on how time is spent, not just total screen time

---

## ⚠️ Limitations
- Dataset is simulated
- May not reflect real-world complexity
- Correlation does not imply causation

---

## 🚀 Future Work
- Build a machine learning model to predict anxiety levels
- Include more real-world features for deeper analysis

---

## 🛠️ Tools Used
- Python
- Pandas
- Matplotlib
- Seaborn