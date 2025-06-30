# mülakat sorusu 

# çift indexte yer alan öğenciler bir listeye, tek indexte olanlar bir listeye alınsın.

# fakat bu iki liste tek bir liste olarak return olmalı 

# çözüm 

students = ["john","mark","venessa","mariam"] 

def divide_students(students):
  groups= [ [] , [] ] 
  for index , student in enumerate(students):
   if index % 2 ==0:
      groups[0].append(student)
else:
     groups[1].append(student)

return groups

divide_students(students)

# enum kullanma örneği : hem sıra numarasına hem de elemanın kendisine aynı anda erişebilirsin.

students = ["john","mark","venessa","mariam"] 

for index , student in enumerate(students):
   print(index,student) 

A = [] 
B = [] 

for index , student in enumerate(students):
   if index % 2 ==0:
      A.append(student)
else:
      B.append(student)

# alternating fonksiyonunu enumerate ile yap 

# çözüm

def alternating_with_enumerate(string):
   new_string = ""
   for i , letter in enumerate(string):
      if i % 2==0:
        new_string +=letter.upper()
        else : 
         new_string += letter.lower() 
