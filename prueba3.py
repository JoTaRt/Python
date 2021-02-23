numero1 = int(input("Dígame el primer numero: "))      #se pide el primer numero
numero2 = int(input("Dígame el segundo numero: "))     #se pide el segundo numero


if(numero1 < numero2):     #se valida que el segundo numero es mayor al primero


    for i in range(numero1+1,numero2):          #se recorre los numeros del primero al segundo
       s = sum(range(numero1+1,numero2))        #se suman los numero desde el siguiente al primero y el penultimo
    print ("la suma es: ",s)

else:
    print ("el numero uno debe ser mayor al segundo numero")


   #**Jose Julian Ramirez**#
   #*JoTaRt*#
   #*jotaj1008r@gmail.com*#
