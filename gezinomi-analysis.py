import pandas as pd
import numpy as np

# 1. Veri setini okuma
df = pd.read_excel("miuul_gezinomi.xlsx")

# 2. Unique şehir sayısı ve frekansları
print("Unique şehir sayısı:", df['SaleCityName'].nunique())
print("Şehir frekansları:\n", df['SaleCityName'].value_counts())

# 3. Unique Concept sayısı
print("\nUnique Concept sayısı:", df['ConceptName'].nunique())

# 4. Concept'lere göre satış sayıları
print("\nConcept satış sayıları:\n", df['ConceptName'].value_counts())

# 5. Şehirlere göre toplam kazanç
print("\nŞehirlere göre toplam kazanç:\n", df.groupby('SaleCityName')['Price'].sum())

# 6. Concept'lere göre toplam kazanç
print("\nConcept'lere göre toplam kazanç:\n", df.groupby('ConceptName')['Price'].sum())

# 7. Şehirlere göre ortalama fiyat
print("\nŞehirlere göre ortalama fiyat:\n", df.groupby('SaleCityName')['Price'].mean())

# 8. Concept'lere göre ortalama fiyat
print("\nConcept'lere göre ortalama fiyat:\n", df.groupby('ConceptName')['Price'].mean())

# 9. Şehir-Concept kombinasyonuna göre ortalama fiyat
print("\nŞehir-Concept kombinasyonuna göre ortalama fiyat:\n", 
      df.groupby(['SaleCityName', 'ConceptName'])['Price'].mean())

# SaleCheckInDayDiff kategorik değişkene dönüştürme
bins = [0, 7, 30, 90, float('inf')]
labels = ['Last Minuters', 'Potential Planners', 'Planners', 'Early Bookers']
df['EB_Score'] = pd.cut(df['SaleCheckInDayDiff'], bins=bins, labels=labels)

# Kontrol
print(df['EB_Score'].value_counts())


# Şehir-Concept-EB Score kırılımında ortalama kazançlar
agg_df = df.groupby(['SaleCityName', 'ConceptName', 'EB_Score']).agg({'Price': ['mean', 'count']})
agg_df.columns = ['mean', 'count']
agg_df.reset_index(inplace=True)

print(agg_df.head())

# City-Concept-Season kırılımında ortalama fiyatlar
agg_df = df.groupby(['SaleCityName', 'ConceptName', 'Seasons'])['Price'].mean().reset_index()
agg_df.sort_values('Price', ascending=False, inplace=True)

print(agg_df.head())

# Eğer indeksler varsa reset_index() ile değişken haline getirme
agg_df.reset_index(drop=True, inplace=True)


# sales_level_based değişkeni oluşturma
agg_df['sales_level_based'] = agg_df.apply(lambda x: 
    f"{x['SaleCityName'].upper()}_{x['ConceptName'].upper().replace(' ', '_')}_{x['Seasons'].upper()}", 
    axis=1)

print(agg_df.head())



# Segment oluşturma
agg_df['SEGMENT'] = pd.qcut(agg_df['Price'], 4, labels=["D", "C", "B", "A"])

# Segment analizi
segment_analysis = agg_df.groupby('SEGMENT').agg({'Price': ['mean', 'max', 'sum', 'count']})
print(segment_analysis


# Antalya'da herşey dahil ve yüksek sezonda tatil yapacak müşteri
new_user = "ANTALYA_HERŞEY_DAHIL_HIGH"
result = agg_df[agg_df['sales_level_based'] == new_user]
print(f"Ortalama gelir: {result['Price'].values[0] if not result.empty else 'Veri bulunamadı'}")

# Girne'de yarım pansiyon ve düşük sezonda tatil yapacak müşteri
new_user2 = "GIRNE_YARIM_PANSIYON_LOW"
result2 = agg_df[agg_df['sales_level_based'] == new_user2]
print(f"Segment: {result2['SEGMENT'].values[0] if not result2.empty else 'Veri bulunamadı'}")
