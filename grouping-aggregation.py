# toplulastırma : özet istatistik veren fonksiyonlar 


count()
first()
mean()
median()
min()
max()
std()

df.groupby("sex")["age"].mean()
df.grouby("sex").agg({"age:"mean"})

df.groupby("sex").agg({"age": ["mean","sum"]}) 

