import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import matplotlib.pyplot as plt
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import precision_score, recall_score, f1_score


df = pd.read_csv("MBA.csv")
col = df.columns
print(df.size)

df["admission"].fillna('Deny', inplace= True)
df["race"].fillna('Unknown', inplace= True)

le = LabelEncoder()
df['admission'] = le.fit_transform(df["admission"])
df = pd.get_dummies(df, columns=["major","race","work_industry","gender"], drop_first= True)

cols =["gpa" , "gmat" , "work_exp"]
sc = StandardScaler()
df[cols] = sc.fit_transform(df[cols])

X = df.drop(columns=["application_id" , "admission"])
y = df["admission"]

X_train , X_test , y_train , y_test = train_test_split(X,y ,test_size= 0.2 , random_state=42)

admission_count = df["admission"].value_counts(normalize=True)
admission_count.plot(kind= 'bar' , color= ["blue", "orange" , "red"])
plt.xlabel("admission status")
plt.ylabel("Proportion")
# plt.show()

smote = SMOTE(random_state=42)
X_train_balanced , y_train_balanced = smote.fit_resample(X_train , y_train)

rf_model = RandomForestClassifier(n_estimators=100 , class_weight="balanced" ,random_state=42)
rf_model.fit(X_train, y_train)
feature_importance = pd.Series(rf_model.feature_importances_, index=X_train.columns)
feature_importance.sort_values(ascending=False).plot(kind="bar", figsize=(8,4), title="Feature Importance")

models = {
    "Logistic Regression": LogisticRegression(class_weight="balanced"),
    "Random Forest": RandomForestClassifier(n_estimators=100, class_weight="balanced", random_state=42),
    "Decision Tree": DecisionTreeClassifier(class_weight="balanced", random_state=42),
    "SVM": SVC(class_weight="balanced")
}

model_scores = {}
for name, model in models.items():
    model.fit(X_train_balanced, y_train_balanced)  # Train model
    y_pred = model.predict(X_test)  # Predict

    precision = precision_score(y_test, y_pred, average="weighted")
    recall = recall_score(y_test, y_pred, average="weighted")
    f1 = f1_score(y_test, y_pred, average="weighted")

    model_scores[name] = {"Precision": precision, "Recall": recall, "F1-score": f1}
    print(f"{name} - Precision: {precision:.4f}, Recall: {recall:.4f}, F1-score: {f1:.4f}")

# Identify the best model based on F1-score
best_model_name = max(model_scores, key=lambda x: model_scores[x]["F1-score"])
print(f"\nBest Model: {best_model_name} based on F1-score")

