caracter = input('caracter a buscar: ')    # pedimos el caracter
cadena = input("cadena: ")                 #pedimos la cadena

if(len(cadena) >= 50):                     #validamos que el minimo de la cadena sea 50

   contar = cadena.count(caracter)           #contamos el numero de caracteres encontrados en la cadena

   print("el numero de ", caracter, " en la cadena es de ", contar)

else:

   print("la cadena es menor a 50 caracteres")


   #**Jose Julian Ramirez**#
   #*JoTaRt*#
   #*jotaj1008r@gmail.com*#
