# In[1]:

import pandas as pd
import numpy as np

# In[3]:

data = pd.read_csv("C:\\Users\\beyza\\OneDrive\\Masaüstü\\VeriBilimi\\country.csv")

# ##  Country.csv dosyasının özelliği
# Bu tablo, çeşitli ülkelerle ilgili bir dizi demografik, ekonomik ve coğrafi veriyi içermektedir. Tabloda her bir satır bir ülkeyi temsil ederken, sütunlar bu ülkelerle ilgili farklı özellikleri gösterir. İşte sütunların anlamları:
# 
# Country: Ülkenin adı.  
# Region: Ülkenin bulunduğu bölge (örneğin, Asya, Doğu Avrupa).  
# Population: Ülkenin toplam nüfusu.  
# Area (sq. mi.): Ülkenin yüzölçümü (mil kare olarak).  
# Pop. Density (per sq. mi.): Nüfus yoğunluğu (mil kare başına düşen kişi sayısı).  
# Coastline (coast/area ratio): Sahil uzunluğunun, ülkenin toplam alanına oranı.  
# Net migration: Net göç oranı (göçmenlerin ülkeye giren veya ülkeden çıkan kişi sayısına göre oranı).  
# Infant mortality (per 1000 births): Bebek ölüm oranı (1000 doğum başına).  
# GDP ($ per capita): Kişi başına düşen Gayri Safi Yurtiçi Hasıla (GSYİH).  
# Literacy (%): Okur-yazarlık oranı.  
# Phones (per 1000): Her 1000 kişi başına düşen telefon sayısı.  
# Arable (%): Tarıma elverişli arazi yüzdesi.  
# Crops (%): Ekilebilir ürünlerin yüzdesi.  
# Other (%): Diğer arazi kullanımı yüzdesi.  
# Climate: Ülkenin iklim kategorisi (numerik bir değer olarak gösterilmiş).  
# Birthrate: Doğum oranı.  
# Deathrate: Ölüm oranı.  
# Agriculture: Tarım sektörünün ekonomideki payı.  
# Industry: Sanayi sektörünün ekonomideki payı.  
# Service: Hizmet sektörünün ekonomideki payı.  


# In[4]:
# ## 1. Görev : Nüfusa Göre Azalan Sırada Sıralama:
print("Nüfusa göre azalan sırada ülkeler:\n ", data.sort_values("Population",ascending=False)[["Country", "Population"]])


# In[5]:
# ## 2. Görev: GDP per capita sütununa göre ülkeleri artan sırada sıralamak(Kişi başına düşen Gayri Safi Yurtiçi Hasıla).
print("GDP per capita sütununa göre artan sırada ülkeler:\n ", data.sort_values("GDP ($ per capita)",ascending=True)[["Country", "GDP ($ per capita)"]])


# In[6]:
# ## 3. Görev: Population sütunu 10 milyonun üzerinde olan ülkeleri seçmek.
print("Nüfusu 10 milyonun üzerinde olan ülkeler: \n ", data[data["Population"]>10000000][["Country", "Population"]])


# In[7]:
# ## 4. Görev: Literacy (%) sütununa göre ülkeleri sıralayıp, en yüksek okur-yazarlık oranına sahip ilk 5 ülkeyi seçmek.
print("En yüksek okur yazarlığa sahip 5 ülke: \n ", data.sort_values("Literacy (%)",ascending=False)[["Country", "Literacy (%)"]].head(5))


# In[8]:
# ## 5. Görev:  Kişi Başı GSYİH 10.000'in Üzerinde Olan Ülkeleri Filtreleme: GDP ( per capita) sütunu 10.000'in üzerinde olan ülkeleri seçmek.
filtered_data=data[data["GDP ($ per capita)"]>10000]
print("Kişi Başı GSYİH 10.000'in üzerinde olan ülkeler:\n ", filtered_data[["Country","GDP ($ per capita)"]])


# In[ ]:
# ## Görev 6 : En Yüksek Nüfus Yoğunluğuna Sahip İlk 10 Ülkeyi Seçme:
# Pop. Density (per sq. mi.) sütununa göre ülkeleri sıralayıp, en yüksek nüfus yoğunluğuna sahip ilk 10 ülkeyi seçmek.
print("En yüksek nüfus yoğunluğuna sahip 10 ülke:\n", data.sort_values("Pop. Density (per sq. mi.)",ascending=False)[["Country","Pop. Density (per sq. mi.)"]].head(10))

