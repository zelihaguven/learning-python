# seaborn : veri görselleştirme de kullanılabilir. yüksek seviyedir. 

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
df = sns.load_dataset("tips")
df.head()

df["sex"].value_counts()
sns.countplot(x=df["sex"] , data=df)
plt.show()

# sayısal değisken görsellestirme

sns.boxplot(x=df["bill"])
plt.show()
