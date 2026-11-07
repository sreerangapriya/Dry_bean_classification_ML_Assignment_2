# Machine Learning Assignment 2 – Dry Bean Classification

## 1. Project Overview

This project implements and compares five machine learning classification algorithms using the Dry Bean Dataset. The objective is to classify different varieties of dry beans based on their physical and geometrical characteristics.

An interactive Streamlit web application has been developed to allow users to upload test data, select a machine learning classification model, and view its evaluation results.

### Problem Statement

The objective of this project is to develop a machine learning classification system that predicts the variety of dry beans using their physical and geometrical characteristics. Five classification algorithms are implemented and compared using multiple evaluation metrics to identify the best-performing model.

## 2. Dataset Description

**Dataset Name:** Dry Bean Dataset

**Source:** UCI Machine Learning Repository

**Dataset Link:** https://archive.ics.uci.edu/dataset/602/dry+bean+dataset

### Dataset Details

- Number of instances: 13,611
- Number of input features: 16
- Number of target classes: 7
- Feature type: Numerical
- Target column: `Class`

The dataset contains measurements such as Area, Perimeter, Major Axis Length, Minor Axis Length, Eccentricity, Convex Area, and other shape-related characteristics.

The seven dry bean classes are:

1. SEKER
2. BARBUNYA
3. BOMBAY
4. CALI
5. HOROZ
6. SIRA
7. DERMASON

## 3. Machine Learning Models Implemented

The following five classification algorithms were trained and evaluated using the same dataset:

1. Logistic Regression
2. Decision Tree Classifier
3. K-Nearest Neighbors (KNN)
4. Gaussian Naive Bayes
5. Support Vector Machine (SVM)

The dataset was divided into training and testing sets using an 80:20 split.

Feature scaling was applied where required. The trained models and label encoder were saved using Joblib for later use in the Streamlit application.

## 4. Evaluation Metrics

The models were evaluated using the following six performance metrics:

- **Accuracy:** Measures the proportion of correctly classified instances.
- **AUC Score:** Measures the model's ability to distinguish between different classes.
- **Precision:** Measures how many predicted classifications are correct.
- **Recall:** Measures how many actual class instances are correctly identified.
- **F1-Score:** Represents the harmonic mean of precision and recall.
- **Matthews Correlation Coefficient (MCC):** Measures the overall quality of classification predictions.

Since this is a multiclass classification problem, precision, recall, and F1-score are evaluated using weighted averaging. AUC is evaluated using a multiclass ROC-AUC approach.

## 5. Model Performance Comparison

The following table presents the evaluation results obtained from the five classification models.

| Machine Learning Model | Accuracy | AUC | Precision | Recall | F1-Score | MCC |
|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | 0.9214 | 0.9934 | 0.9222 | 0.9214 | 0.9216 | 0.9050 |
| Decision Tree | 0.8917 | 0.9330 | 0.8912 | 0.8917 | 0.8913 | 0.8691 |
| KNN | 0.9166 | 0.9812 | 0.9174 | 0.9166 | 0.9168 | 0.8992 |
| Naive Bayes | 0.7639 | 0.9644 | 0.7654 | 0.7639 | 0.7615 | 0.7154 |
| Support Vector Machine | **0.9221** | **0.9937** | **0.9224** | **0.9221** | **0.9222** | **0.9059** |

## 6. Model Performance Observations

### 6.1 Logistic Regression

Logistic Regression achieved an accuracy of 92.14% and an AUC of 0.9934. It provided strong classification performance and a high MCC value of 0.9050.

### 6.2 Decision Tree

The Decision Tree classifier achieved an accuracy of 89.17%. Its performance was comparatively lower than Logistic Regression, KNN, and SVM.

### 6.3 K-Nearest Neighbors

KNN achieved an accuracy of 91.66% and an AUC of 0.9812. It demonstrated good classification performance, although it did not outperform SVM.

### 6.4 Gaussian Naive Bayes

Gaussian Naive Bayes achieved an accuracy of 76.39%. It recorded comparatively lower precision, recall, F1-score, and MCC values among the five models.

### 6.5 Support Vector Machine

Support Vector Machine achieved the highest accuracy of 92.21%, AUC of 0.9937, precision of 0.9224, recall of 0.9221, F1-score of 0.9222, and MCC of 0.9059.

It demonstrated the best overall classification performance among the five models.

## 7. Overall Best-Performing Model

**Support Vector Machine (SVM)** was identified as the overall best-performing model based on the evaluation results.

It achieved the highest values across all six reported evaluation metrics. Therefore, SVM is selected as the best-performing model for the Dry Bean classification task.

## 8. Streamlit Web Application

An interactive Streamlit web application was developed to evaluate the trained classification models.

### Application Features

- Upload a labelled test dataset in CSV format.
- Select one of the five trained machine learning models.
- Display Accuracy, AUC, Precision, Recall, F1-Score, and MCC.
- Display the confusion matrix.
- Display the classification report.
- View prediction results.
- Download prediction results as a CSV file.

The application loads the previously saved models and evaluates the uploaded test dataset without retraining the models.

### Live Application Link

https://drybeanclassificationmlassignment2-jnnwqoywtafyxnkfjredyq.streamlit.app/

## 9. Project Structure

```text
Dry_bean_classification_ML_Assignment_2/
│
├── app.py
├── train.py
├── requirements.txt
├── README.md
├── test_data.csv
├── metrics_comparison.csv
│
└── model/
    ├── logistic_regression.joblib
    ├── decision_tree.joblib
    ├── knn.joblib
    ├── naive_bayes.joblib
    ├── svm.joblib
    └── label_encoder.joblib
```

The model folder contains all five trained classification models and the label encoder required for prediction.

## 10. Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib
- Joblib
- GitHub
- Streamlit Community Cloud

## 11. Installation and Execution

### Step 1: Clone the Repository

```bash
git clone https://github.com/sreerangapriya/Dry_bean_classification_ML_Assignment_2.git
```

### Step 2: Navigate to the Project Folder

```bash
cd Dry_bean_classification_ML_Assignment_2
```

### Step 3: Install Required Packages

```bash
pip install -r requirements.txt
```

### Step 4: Train the Models

```bash
python train.py
```

This generates the trained model files, test dataset, and model comparison results.

The original Dry Bean dataset Excel file must also be available in the project folder before running the training script.

### Step 5: Run the Streamlit Application

```bash
python -m streamlit run app.py
```

The application opens in the browser and allows users to upload test data and evaluate the selected classification model.

## 12. GitHub Repository

**GitHub Repository Link:**

https://github.com/sreerangapriya/Dry_bean_classification_ML_Assignment_2

The repository contains the project source code, trained models, preprocessing artifacts, requirements file, test dataset, and project documentation.

## 13. Live Streamlit Application

**Deployed Streamlit Application Link:**

https://drybeanclassificationmlassignment2-jnnwqoywtafyxnkfjredyq.streamlit.app/

The application is deployed using Streamlit Community Cloud and provides an interactive interface for evaluating the five trained classification models.

## 14. Conclusion

This project demonstrates the implementation and comparison of five machine learning classification algorithms using the Dry Bean Dataset.

The models were evaluated using six performance metrics: Accuracy, AUC, Precision, Recall, F1-Score, and Matthews Correlation Coefficient.

Based on the obtained results, Support Vector Machine achieved the best overall performance, followed closely by Logistic Regression and K-Nearest Neighbors.

The Streamlit application provides an interactive interface for uploading test data and evaluating the trained classification models. This project demonstrates the practical application of machine learning algorithms, model evaluation, and web application development.

