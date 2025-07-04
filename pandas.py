import pandas as pd

# pandas serileri bir veri yapısıdır ! 

s=pd.Series([10,7,12,4,5]) 

s.index 
s.dtype
s.size
s.ndim # boyut 

# pandas serileri tek boyutlu 

s.values 

type(s.values)

# bu numpy.ndarray olarak döner
