# iloc ve loc : 

# index bilgisi vererek seçim : iloc 

# loc ise indexteki labela göre 

import pandas as pd 
import seaborn as sns
pd.set_option('display.max_columns' , none)
df = sns.load_dataset("example")
df.head

#iloc : 

df.iloc[0:3] # klasik seçim  : üç burada olmaz 
df.iloc[0,0] 

# loc : 

df.loc[0:3]
# 0 1 2 3. indeksleri verir 
# label based selection yapıldı 
