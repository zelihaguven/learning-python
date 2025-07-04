import pandas as pd
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)
subset = df.loc[0:1, ['A', 'B']] 

# Yukarıdaki kod dizisi hangi çıktıyı hedefliyor? 

# 0 ve 1. satırları, 'A' ve 'B' sütunlarını seçer


import pandas as pd

data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)
subset = df.iloc[0:2, [0, 1]] 

# Yukarıdaki kodun çıktısı algoritma emri nedir ?

# İlk iki satırı ve ilk iki sütunu seçer

# Onur cinsiyetlere göre mutluluk oranlarını ölçen bir veri setini bir de yaşlara göre analiz etmek istiyor. 
# Hangi Pandas metodu Onur’un işini kolaylaştırır?

# pivot table 
