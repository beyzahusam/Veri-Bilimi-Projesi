import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C:\\Users\\beyza\\OneDrive\\Masaüstü\\VeriBilimi\\50_Startups.csv")
data.head()

# R&D Harcaması ve Kâr Arasındaki İlişki (Scatter Plot): Ar-Ge harcamaları ile kâr arasındaki ilişkiyi gösteren bir dağılım grafiği.

plt.figure(figsize=(6,4))
plt.scatter(data["R&D Spend"], data["Profit"], color="blue", alpha=0.6)
plt.xlabel("R&D Spend")
plt.ylabel("Profit")
plt.title("R&D Harcaması vs Kâr")
plt.show()

# Yönetim Harcamaları ve Kâr Arasındaki İlişki (Scatter Plot): Yönetim harcamaları ile kâr arasındaki ilişkiyi gösteren bir dağılım grafiği.

plt.figure(figsize=(6,4))
plt.scatter(data["Administration"], data["Profit"], color="green", alpha=0.6)
plt.xlabel("Administration Spend")
plt.ylabel("Profit")
plt.title("Yönetim Harcaması vs Kâr")
plt.show()

# Eyaletlere Göre Ortalama Kâr (Bar Chart): Farklı eyaletlerdeki startup'ların ortalama kârlarını karşılaştıran bir çubuk grafik.

state_profit = data.groupby("State")["Profit"].mean()
plt.figure(figsize=(6,4))
state_profit.plot(kind="bar", color="orange", edgecolor="black")
plt.ylabel("Ortalama Kâr")
plt.title("Eyaletlere Göre Ortalama Kâr")
plt.show()

# Harcama Türlerinin Karşılaştırması (Boxplot): R&D, yönetim ve pazarlama harcamalarının dağılımını karşılaştıran bir kutu grafiği.

plt.figure(figsize=(8,5))
data[["R&D Spend", "Administration", "Marketing Spend"]].boxplot()
plt.title("Harcamaların Dağılımı (Boxplot)")
plt.ylabel("Harcama Miktarı")
plt.show()
