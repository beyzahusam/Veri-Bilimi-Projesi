import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\beyza\\OneDrive\\Masaüstü\\VeriBilimi\\dava_sonuclari.csv")

#Eksik değer kontrolü
total_missing = df.isnull().sum().sum()
print("\nEksik değer sayısı :", total_missing)
if total_missing > 0:
    df = df.fillna(df.mean(numeric_only=True))
    print(f"{total_missing} eksik değer sütun ortalamaları ile dolduruldu.")
else:
    print("Eksik değer yok.")

#Aykırı değer silme
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
outlier_found = False 

for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower) | (df[col] > upper)]
    
    if not outliers.empty:
        print(f"{col} sütununda {len(outliers)} tane aykırı değer var.")
        outlier_found = True
    df = df[(df[col] >= lower) & (df[col] <= upper)]

if not outlier_found:
    print("Veri setinde aykırı değer yok.")

#One hot encoding
df = pd.get_dummies(df, columns=["Case Type"], drop_first=True)

y = df["Severity"]
X = df.drop(columns=["Severity", "Outcome"]) 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier(random_state=42,max_depth=7,min_samples_split=5,min_samples_leaf=3,criterion='entropy',class_weight='balanced')
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

#Değerlerin hesaplanması
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)

print("\nModel Performansı:")
print(f"Accuracy: {accuracy:.3f}")
print(f"Precision: {precision:.3f}")
print(f"Recall: {recall:.3f}")
print(f"F1-Score: {f1:.3f}")
print(classification_report(y_test, y_pred, zero_division=0))

#Karar ağacı görselleştirilmesi
plt.figure(figsize=(22,10))
plot_tree(model, feature_names=X.columns, class_names=[str(c) for c in sorted(y.unique())], filled=True)
plt.title("Karar Ağacının Görselleştirilmesi")
plt.show()

#Özelliklerin önem sırasına göre yazılması
importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': model.feature_importances_
}).sort_values(by='Importance', ascending=False)
print("\nÖzellik önem sıralaması:")
print(importance)




