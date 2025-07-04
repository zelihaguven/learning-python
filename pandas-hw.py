# Titanic Veri Seti Çözümleri

import seaborn as sns
import pandas as pd

# Görev 1: Titanic veri setini yükleme
titanic = sns.load_dataset('titanic')

# Görev 2: Kadın ve erkek yolcu sayıları
print(titanic['sex'].value_counts())

# Görev 3: Her sütundaki unique değer sayıları
print(titanic.nunique())

# Görev 4: pclass unique değer sayısı
print(titanic['pclass'].nunique())

# Görev 5: pclass ve parch unique değer sayıları
print(titanic[['pclass', 'parch']].nunique())

# Görev 6: embarked tipini category yapma
print(titanic['embarked'].dtype)
titanic['embarked'] = titanic['embarked'].astype('category')
print(titanic['embarked'].dtype)

# Görev 7: embarked'ı C olanlar
print(titanic[titanic['embarked'] == 'C'])

# Görev 8: embarked'ı S olmayanlar
print(titanic[titanic['embarked'] != 'S'])

# Görev 9: Yaşı 30'dan küçük kadınlar
print(titanic[(titanic['age'] < 30) & (titanic['sex'] == 'female')])

# Görev 10: Fare > 500 veya yaş > 70
print(titanic[(titanic['fare'] > 500) | (titanic['age'] > 70)])

# Görev 11: Boş değerlerin toplamı
print(titanic.isnull().sum())

# Görev 12: who değişkenini çıkarma
titanic.drop('who', axis=1, inplace=True)

# Görev 13: deck boş değerleri mod ile doldurma
titanic['deck'] = titanic['deck'].fillna(titanic['deck'].mode()[0])

# Görev 14: age boş değerleri medyan ile doldurma
titanic['age'] = titanic['age'].fillna(titanic['age'].median())

# Görev 15: survived için pclass ve cinsiyet kırılımında istatistikler
print(titanic.groupby(['pclass', 'sex'])['survived'].agg(['sum', 'count', 'mean']))

# Görev 16: age_flag oluşturma
titanic['age_flag'] = titanic['age'].apply(lambda x: 1 if x < 30 else 0)


# Tips Veri Seti Çözümleri

# Görev 17: Tips veri setini yükleme
tips = sns.load_dataset('tips')

# Görev 18: Time'a göre total_bill istatistikleri
print(tips.groupby('time')['total_bill'].agg(['sum', 'min', 'max', 'mean']))

# Görev 19: Günlere ve time'a göre total_bill istatistikleri
print(tips.groupby(['day', 'time'])['total_bill'].agg(['sum', 'min', 'max', 'mean']))

# Görev 20: Lunch zamanı ve kadın müşteriler için istatistikler
lunch_female = tips[(tips['time'] == 'Lunch') & (tips['sex'] == 'Female')]
print(lunch_female.groupby('day')[['total_bill', 'tip']].agg(['sum', 'min', 'max', 'mean']))

# Görev 21: size < 3 ve total_bill > 10 olan siparişlerin ortalaması
filtered = tips[(tips['size'] < 3) & (tips['total_bill'] > 10)]
print(filtered.mean(numeric_only=True))

# Görev 22: total_bill_tip_sum oluşturma
tips['total_bill_tip_sum'] = tips['total_bill'] + tips['tip']

# Görev 23: İlk 30 kişiyi yeni dataframe'e atama
sorted_tips = tips.sort_values('total_bill_tip_sum', ascending=False)
top_30 = sorted_tips.head(30) 
