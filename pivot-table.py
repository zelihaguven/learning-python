# pivot table : groupby islemleri gibi kırılım acısından değerlendirmeye yarar. 

df.pivot_table("survived","sex","embarked", aggfunc="std")

df.pivot_table("survived","sex", ["embarked", "class"])

# bu kullanımda sex kısmına boyut vermediğimiz için orası tek boyutlu/seviyeli olur


