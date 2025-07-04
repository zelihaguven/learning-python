# Frequency Table
df['kategori'].value_counts()

# Relative Frequency
df['kategori'].value_counts(normalize=True)

# Cross Tabulation / Crosstab
pd.crosstab(df['cinsiyet'], df['sonuç'])


# Gruplama ve Toplama (Groupby & Aggregation)
df.groupby('şehir')['maas'].mean()

# Label Encoding / One-Hot Encoding (Analize Hazırlık)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['kategori_encoded'] = le.fit_transform(df['kategori'])
