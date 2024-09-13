#Fatiamento de strings

#        0123456789      16
texto = "Aprendendo python"
print(texto[0:16]) #16 é EXCLUSIVO
print(texto[0:17])

print(texto[0])
print(texto[1])
print(texto[2])

print(texto[11:17])  #python
print(texto[11:])    #python

print(texto[0:10])   #Aprendendo
print(texto[:10])    #Aprendendo

print(texto[:])      # do inicio ao final
print(texto)

print(texto[0:17:2])  #imprime caracteres pares
print(texto[::2])     #imprime caracteres pares

print(texto[-1])      #último caractere
print(texto[::-1])    #Inverte a ordem