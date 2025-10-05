import pandas as pd
import numpy as np

data = pd.read_csv("C:\\Users\\beyza\\OneDrive\\Masaüstü\\VeriBilimi\\country.csv")

# Nüfusa göre azalan sırada sıralama:
print("Nüfusa göre azalan sırada ülkeler:\n ", data.sort_values("Population",ascending=False)[["Country", "Population"]])


# GDP per capita sütununa göre ülkeleri artan sırada sıralama (Kişi başına düşen Gayri Safi Yurtiçi Hasıla):
print("GDP per capita sütununa göre artan sırada ülkeler:\n ", data.sort_values("GDP ($ per capita)",ascending=True)[["Country", "GDP ($ per capita)"]])


# Population sütunu 10 milyonun üzerinde olan ülkeleri seçme:
print("Nüfusu 10 milyonun üzerinde olan ülkeler: \n ", data[data["Population"]>10000000][["Country", "Population"]])


# Literacy (%) sütununa göre ülkeleri sıralayıp, en yüksek okur-yazarlık oranına sahip ilk 5 ülkeyi seçme:
print("En yüksek okur yazarlığa sahip 5 ülke: \n ", data.sort_values("Literacy (%)",ascending=False)[["Country", "Literacy (%)"]].head(5))


# Kişi Başı GSYİH 10.000'in Üzerinde Olan Ülkeleri Filtreleme: GDP ( per capita) sütunu 10.000'in üzerinde olan ülkeleri seçme:
filtered_data=data[data["GDP ($ per capita)"]>10000]
print("Kişi Başı GSYİH 10.000'in üzerinde olan ülkeler:\n ", filtered_data[["Country","GDP ($ per capita)"]])


# Pop. Density (per sq. mi.) sütununa göre ülkeleri sıralayıp, en yüksek nüfus yoğunluğuna sahip ilk 10 ülkeyi seçme:
print("En yüksek nüfus yoğunluğuna sahip 10 ülke:\n", data.sort_values("Pop. Density (per sq. mi.)",ascending=False)[["Country","Pop. Density (per sq. mi.)"]].head(10))

