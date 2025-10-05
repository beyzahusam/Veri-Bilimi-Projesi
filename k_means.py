import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from kneed import KneeLocator
from sklearn.decomposition import PCA

data = pd.read_csv("C:\\Users\\beyza\\OneDrive\\Masaüstü\\VeriBilimi\\dava.csv")

sns.set_theme(style="whitegrid")

#Kümeleme için özellikler seçilir
features = ['Case Duration (Days)', 'Number of Witnesses',
            'Legal Fees (USD)', 'Number of Evidence Items', 'Severity']
X = data[features]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
inertia = []
K_range = range(1, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init='auto')
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

#KneeLocator ile optimal küme sayısı belirlenir
knee = KneeLocator(list(K_range), inertia, curve='convex', direction='decreasing')
optimal_k = knee.knee if knee.knee is not None else 3
print(f"Optimal küme sayısı: {optimal_k}")

plt.figure(figsize=(8,5))
plt.plot(K_range, inertia, marker='o')
plt.axvline(x=optimal_k, color='red', linestyle='--', label=f'Optimal k = {optimal_k}')
plt.title("Elbow Yöntemi ile Optimal Küme Sayısı")
plt.xlabel("Küme Sayısı (k)")
plt.ylabel("Toplam Hata Kareleri")
plt.legend()
plt.show()

#Veri kümelere göre ayrılır
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init='auto')
data['Cluster'] = kmeans.fit_predict(X_scaled)

cluster_summary = data.groupby('Cluster')[features].mean()
print("\nKümelere göre ortalama değerler:")
print(cluster_summary)
print("\nKüme dağılımı :")
print(data['Cluster'].value_counts())

plt.figure(figsize=(16,10))
for i, feature in enumerate(features):
    plt.subplot(2, 3, i+1)
    sns.boxplot(x='Cluster', y=feature, hue='Cluster', data=data, palette='Set1', dodge=False, legend=False)
    plt.title(f"{feature} dağılımı ")
plt.tight_layout()
plt.show()

#2boyuta indirgenerek verilerin kümelere görse görselleştirilmesi yapılır
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
data['PCA1'] = X_pca[:,0]
data['PCA2'] = X_pca[:,1]

plt.figure(figsize=(8,6))
sns.scatterplot(x='PCA1', y='PCA2', hue='Cluster', data=data, palette='Set1', s=100)
plt.title("Tüm Özellikler")
plt.show()
