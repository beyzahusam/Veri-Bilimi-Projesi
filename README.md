# Veri Bilimi Ödevleri ve Projesi

Bu repo, eğitime verilen ödevlerin kodlarını, görsellerini ve analizlerini içermektedir.  
Her ödev, farklı veri setleri üzerinde veri analizi, görselleştirme ve makine öğrenmesi tekniklerinin uygulanmasını amaçlar.

---

## Genel Amaç

Bu ödevler kapsamında:
- Veri analizi ve veri görselleştirme tekniklerini uygulanmış,
- Makine öğrenmesi algoritmaları kullanılmış,
- Python veri bilimi kütüphaneleriyle (pandas, matplotlib, seaborn, scikit-learn vb.) pratik yapılmıştır.

---

## 📊 1. Veri Görselleştirme Ödevi (`50_Startups.csv`)

Bu ödevde, **startup verileri** üzerinde temel veri görselleştirme teknikleri uygulanmıştır.  
R&D, yönetim ve pazarlama harcamaları ile kâr arasındaki ilişkiler incelenmiş, eyaletlere göre ortalama kârlar karşılaştırılmıştır.  
Veriler grafiklerle analiz edilerek **harcamalar ve kâr arasındaki ilişki** yorumlanmıştır.

---
## 🌳 2. Decision Tree Ödevi (`dava_sonuclari.csv`)

Bu ödevde, dava sonuçları veri seti üzerinde bir **Decision Tree (Karar Ağacı)** modeli kurulmuştur.  
Veri ön işleme aşamalarında eksik ve aykırı değerler kontrol edilmiş, eğitim (%80) ve test (%20) verisi ayrımı yapılmıştır.  
Modelin başarımı **Accuracy, Precision, Recall ve F1-Score** metrikleriyle değerlendirilmiştir.  
Son olarak, karar ağacı görselleştirilmiş ve modelin tahminlerinde **en etkili özellikler** analiz edilmiştir.

---

## 🧮 3. K-Means Kümeleme Ödevi (`dava.csv`)

Bu ödevde, dava verileri üzerinde **K-Means kümeleme algoritması** uygulanmıştır.  
Uygun özellikler seçilerek veri kümelenmiş, **Elbow yöntemi** ile optimal küme sayısı belirlenmiştir.  
Sonuçlar grafiklerle görselleştirilmiş ve elde edilen kümelerin anlamlılığı yorumlanmıştır.

---

## 🌍 4. Veri Filtreleme & Sıralama Projesi (`country.csv`)

Bu bölümde, `country.csv` veri seti kullanılarak çeşitli **filtreleme, sıralama ve seçim işlemleri** yapılmıştır.  
Nüfus, GDP per capita, okuryazarlık oranı ve nüfus yoğunluğu gibi göstergelere göre ülkeler filtrelenmiş ve sıralanmıştır.  

---

## 🛠️ Kullanılan Teknolojiler
- Python 3.13.0
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn