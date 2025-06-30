# uygulama - mülakat sorusu

#çift indeksteki harf, büyük harf olacak. bunu sağlayan bir fonksiyonu yazmaya çalış.

def alternate(string):
  new_string = "" #değiştirmelerimi ekleyebilmem için yeni string  
  #for döngüsünün gezeceği yer için range kullanabilirim. 
  for string_index in range(len(string)):
       if  string_index % 2 ==0: #aldığım index çiftse
         new_string += string[string_index].upper() #büyütmeyi yapıyorum 
        else : 
           new_string += string[string_index].lower() 
  print(new_string) 

  alternate("try")
 # TrY
         
         
           
     
    
