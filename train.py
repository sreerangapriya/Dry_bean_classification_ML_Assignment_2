
import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

from sklearn.metrics import (
    accuracy_score,
    roc_auc_score,
    precision_score,
    recall_score,
    f1_score,
    matthews_corrcoef
)

# ------------------------------------------------
# 1. LOAD DATASET
# ------------------------------------------------

print("Loading Dry Bean Dataset...")

DATASET_FILE = "Dry_Bean_Dataset.xlsx"

if not os.path.exists(DATASET_FILE):
    raise FileNotFoundError(
        "Dry_Bean_Dataset.xlsx not found. "
        "Place the Excel dataset in the project folder."
    )

df = pd.read_excel(DATASET_FILE)

print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)

# Remove unnecessary spaces from column names
df.columns = df.columns.str.strip()

# ------------------------------------------------
# 2. SEPARATE FEATURES AND TARGET
# ------------------------------------------------

target_column = "Class"

if target_column not in df.columns:
    raise ValueError("Target column 'Class' was not found.")

df = df.dropna(subset=[target_column])

X = df.drop(columns=[target_column])
X = X.apply(pd.to_numeric, errors="raise")

if X.isnull().any().any():
    raise ValueError("Input features contain missing values.")

y = df[target_column].astype(str).str.strip()

print("Number of input features:", X.shape[1])
print("Number of instances:", X.shape[0])
print("Number of classes:", y.nunique())

if X.shape[1] < 12 or X.shape[0] < 500:
    raise ValueError("Dataset does not meet minimum requirements.")

# Encode target classes
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)
joblib.dump(encoder, "model/label_encoder.joblib")

# ------------------------------------------------
# 3. SPLIT DATASET
# ------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.20,
    random_state=42,
    stratify=y_encoded
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

# ------------------------------------------------
# 4. CREATE MODEL FOLDER
# ------------------------------------------------

os.makedirs("model", exist_ok=True)

# ------------------------------------------------
# 5. DEFINE CLASSIFICATION MODELS
# ------------------------------------------------

models = {
    "Logistic Regression": Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", LogisticRegression(max_iter=3000))
    ]),

    "Decision Tree": DecisionTreeClassifier(
        random_state=42
    ),

    "KNN": Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", KNeighborsClassifier(n_neighbors=5))
    ]),

    "Naive Bayes": GaussianNB(),

    "Support Vector Machine": Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", SVC(
            probability=True,
            random_state=42
        ))
    ])
}

model_files = {
    "Logistic Regression": "logistic_regression.joblib",
    "Decision Tree": "decision_tree.joblib",
    "KNN": "knn.joblib",
    "Naive Bayes": "naive_bayes.joblib",
    "Support Vector Machine": "svm.joblib"
}

# ------------------------------------------------
# 6. TRAIN AND EVALUATE MODELS
# ------------------------------------------------

results = []

print("\nStarting model training...\n")

for model_name, model in models.items():

    print("Training:", model_name)

    # Train model
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Prediction probabilities
    y_prob = model.predict_proba(X_test)

    # Evaluation metrics
    accuracy = accuracy_score(y_test, y_pred)

    auc = roc_auc_score(
        y_test,
        y_prob,
        multi_class="ovr",
        average="weighted"
    )

    precision = precision_score(
        y_test, y_pred, average="weighted",
        zero_division=0
    )

    recall = recall_score(
        y_test, y_pred, average="weighted",
        zero_division=0
    )

    f1 = f1_score(
        y_test, y_pred, average="weighted",
        zero_division=0
    )

    mcc = matthews_corrcoef(y_test, y_pred)

    # Save trained model
    model_path = os.path.join(
        "model", model_files[model_name]
    )

    joblib.dump(model, model_path)

    # Store evaluation results
    results.append({
        "ML Model Name": model_name,
        "Accuracy": accuracy,
        "AUC": auc,
        "Precision": precision,
        "Recall": recall,
        "F1": f1,
        "MCC": mcc
    })

    print("Accuracy:", round(accuracy, 4))
    print("AUC:", round(auc, 4))
    print("Precision:", round(precision, 4))
    print("Recall:", round(recall, 4))
    print("F1 Score:", round(f1, 4))
    print("MCC:", round(mcc, 4))
    print("Model saved successfully!\n")

# ------------------------------------------------
# 7. SAVE TEST DATA
# ------------------------------------------------

test_data = X_test.copy()

test_data[target_column] = encoder.inverse_transform(y_test)

test_data.to_csv("test_data.csv", index=False)

# ------------------------------------------------
# 8. SAVE METRICS COMPARISON
# ------------------------------------------------

results_df = pd.DataFrame(results)

results_df.to_csv(
    "metrics_comparison.csv",
    index=False
)

print("\nFINAL MODEL COMPARISON")
print(results_df.to_string(index=False))

print("\nAll five models trained successfully!")
print("Five model files saved inside model folder.")
print("test_data.csv generated successfully.")
print("metrics_comparison.csv generated successfully.")
