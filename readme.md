# Developer Productivity Performance Analysis Model

## 📌 Project Objective

The objective of this project is to analyze and predict **software developer task success** by studying how **work patterns, human factors, code quality metrics, and AI usage** influence overall developer performance.

This project aims to:
- Identify key factors that impact developer productivity and task success
- Understand the role of stress, sleep, cognitive load, and work habits
- Analyze code quality indicators such as bugs, errors, and commits
- Build a machine learning model to predict **Task Success Rate**, the target variable

---
## project workflow 
1. Data ingestion
2. Exploratory Data Analysis
3. Data preprocessing
4. Model Building
5. Model Evaluation
6. Model Deployment
---
## 📊 Data Information

The dataset contains information related to developer work behavior, human factors, and coding performance.  
Each row represents a developer task instance.

- Size: 1000 rows × 13 columns

- No missing values: All features are complete.

- Data types: Mostly integer (int64) with a few float columns (Sleep_Hours, Task_Duration_Hours).

### Features
- **Hours_Coding** – Time spent coding  
- **Lines_of_Code** – Size of code written  
- **Bugs_Found** – Number of bugs identified  
- **Bugs_Fixed** – Number of bugs resolved  
- **AI_Usage_Hours** – Time spent using AI tools  
- **Sleep_Hours** – Daily sleep duration  
- **Cognitive_Load** – Mental workload level  
- **Coffee_Intake** – Coffee consumption  
- **Stress_Level** – Developer stress level  
- **Task_Duration_Hours** – Time taken to complete tasks  
- **Commits** – Number of code commits  
- **Errors** – Coding errors encountered  

### Target Variable
- **Task_Success_Rate** – Measures how successfully a developer completes assigned tasks

---

## Final Result

- A **Random Forest Regressor** was used as the final machine learning model.
- The model captured **non-linear relationships** between human factors, work patterns, and task success.
- Analysis shows that **developer performance is influenced more by efficiency, code quality, stress, and sleep** than by coding hours alone.
- The model achieved a **94.5 R² score**, indicating meaningful predictive performance.
