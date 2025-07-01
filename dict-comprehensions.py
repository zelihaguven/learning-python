
# mülakat sorusu
# amaç : çift sayıların karesi alınarak bir sözlüğe eklenmek istenmektedir. 

# çözüm : keyler orijinal değerler valuelar ise değiştirilmiş değerler olacak.

numbers_range(10)
new_dict = {}

for n in numbers : 
  if n%2==0 :
     new_dict[n] = n ** 2

#output : {0:0 , 2:4, 4:16, 6:36, 8 : 64} 

# daha iyi çözüm : 

{ n : n **2 for n in numbers if n%2 ==0} 

# {key_expression: value_expression for item in iterable if condition}

