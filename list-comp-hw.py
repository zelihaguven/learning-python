# Görev 1: Numeric değişken isimlerini büyük harfe çevirme ve NUM ekleme

import seaborn as sns
df = sns.load_dataset("car_crashes")

# Tüm sütun isimlerini büyük harfe çevirip başına NUM ekleme
new_columns = ['NUM_' + col.upper() for col in df.columns]
print(new_columns)

Görev 2: İçinde "no" geçmeyen değişkenlere FLAG ekleme

import seaborn as sns
df = sns.load_dataset("car_crashes")

# Görev 2 : 'no' içermeyen sütunlara FLAG ekleme (tümü büyük harf)
new_columns = [col.upper() + '_FLAG' if 'no' not in col.lower() else col.upper() for col in df.columns]
print(new_columns)

# Görev 3: Belirtilen değişkenlerden farklı olanları seçme

import seaborn as sns
df = sns.load_dataset("car_crashes")

og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
print(new_df.head())

