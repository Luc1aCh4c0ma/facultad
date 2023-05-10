import random
MSJ = ""
import os
from math import sqrt

def menu ():
    print ("operaciones matematicas")
    print ("seleccione que quiere resolver:")
    print ("1) Rectas paralelas y perpendiculares a una dada")
    print ("2) Analisis de una funcion lineal")
    print ("3) Analisis de una funcion cuadratica")
    print ("4) Salir")
    op = input ("Escriba la opcion:") 
    op = int (op)
    if op==1 : rectaspyp ()
    elif op==2: funcionlineal ()
    elif op==3: funcioncuadratica ()
    else: exit ()

def rectaspyp ():
    os.system ("cls")
    print ("")
    print ("usted selecciono la opcion - rectas paralelas y perpendiculares de una dada -")
    num1 = input ("ingrese coeficiente principal: ")
    num2 = input ("ingrese termino independiente: ")
    num1 = float (num1)
    num2 = float (num2)
    print ("\n"*1)
    print ("RECTAS PARALELAS:")
    print ("y=", num1, "x +", num2 + random.randint (1,6))
    print ("y=", num1, "x +", num2 + random.randint (6,11))
    print ("y=", num1, "x +", num2 + random.randint (11,16))
    print ("\n"*1)
    MSJ = "CONDICION DE PARALELISMO: \n la pendiente es igual en todas las rectas \n el usuario definió a m = " + str(num1)
    print (MSJ)
    print ("\n"*2)
    print ("RECTAS PERPENDICULARES:")
    print ("y = ", -1/num1, "x +", num2 + random.randint (1,6))
    print ("y = ", -1/num1, "x +", num2 + random.randint (6,11))
    print ("y = ", -1/num1, "x +", num2 + random.randint (11,16))
    print ("\n"*1)
    MSJ = "CONDICION DE PERPENDICULARIDAD: \n la pendiente de la recta es la inversa aditiva de la anterior \n "
    print (MSJ)
    print ("\n"*2)  
    menu ()


def funcionlineal ():
    os.system ("cls")
    print ("")
    print ("usted selecciono la opcion - funcion lineal -")
    num1 = input ("ingrese coeficiente principal: ")
    num2 = input ("ingrese termino independiente: ")
    num1 = float (num1)
    num2 = float (num2)
    cortex = -num2/num1
    cortey = num2
    print ("\n"*1)
    print ("calculamos la intercepcion:")
    print ("x = -b/m")
    print ("y = b")
    print ("x=", -num2/num1)
    print ("y=",num2)
    print ("\n"*1)
    print ("por lo que: ")

    if num1 > 0:
        print ("El comportamiento de la recta es: CRECIENTE")
    elif num1 < 0:
        print ("el comportamiento de la recta es: DECRECIENTE")
    else:
        print ("el comportamiento de la recta es: CONSTANTE")
    
    print ("CORTE EN EJE X = ", (cortex,",0"), "\n", "CORTE EN EJE Y = ", ("0,",cortey))
    print ("\n"*1)
    menu ()


def funcioncuadratica ():
    os.system ("cls")
    print ("")
    print ("usted selecciono la opcion - analisis de una funcion cuadratica -")
    num1 = input ("ingrese coeficiente principal: ")
    num2 = input ("ingrese coeficiente lineal: ")
    num3 = input ("ingrese el termino independiente: ")
    num1 = float (num1)
    num2 = float (num2)
    num3 = float (num3)
    print ("calculamos el discriminante -> b²-4ac :")
    print (num2,"²","-4x",num1,"x",num3)
    discriminante = num2**2 - 4*num1*num3
    print ("resultado = ", discriminante)
    print ("")

    if discriminante < 0 :
        print ("LA ECUACION NO TIENE SOLUCIONES REALES")
    elif discriminante == 0:
        x= -num2/(2*num1)
        print ("LA ECUACION TIENE UNA SOLUCION REAL REPETIDA", "\n", "x1,x2 = ", x)
    else:
        x1 = (-num2+sqrt(num2**2-(4*num1*num3)))/(2*num1)  # Fórmula de Bhaskara parte positiva
        x2 = (-num2-sqrt(num2**2-(4*num1*num3)))/(2*num1)  # Fórmula de Bhaskara parte negativa
        print ("LA ECUACION TIENE DOS SOLUCIONES REALES DISTINTAS")
        print("Las soluciones de la ecuación son:")
        print("x1= ", x1)
        print("x2=", x2)
    
    print ("calculamos corte en eje y: ")
    resultcortey = (0*num1**2+num2*0+num3)
    print ("y= ", resultcortey) 
    
    
    print ("CALCULAMOS EL VERTICE -> y = ax² + bx + c")
    print ("y = ", num1,"x² + ", num2,"x +", num3)
    print ("x= -b/2a", "->", "x= ", -num2,"/2*", num1)
    resultadox = (-num2) / (2*num1)
    print ("reemplazamos x en la ecuación:")
    print ("y= ", num1, "x", resultadox,"² + ", num2,"x", resultadox," + ", num3)
    resultadoy= num1*resultadox**2+num2*resultadox+num3
    print ("x = ", resultadox)
    print ("y = ", resultadoy)

    if num1 > 0:
        print ("LA CONCAVIDAD ES POSITIVA (se abre hacia arriba)")
        print ("DETERMINAMOS INTERVALO DE DECRECIMIENTO")
        intercrec = ("∞,", resultadox)
        print (intercrec)
        print ("DETERMINAMOS INTERVALO DE CRECIMIENTO")
        interdec = (resultadox, "∞,")
        print (interdec)
    else:
        print ("LA CONCAVIDAD ES NEGATIVA (se abre hacia abaj0)")
        print ("DETERMINAMOS INTERVALO DE DECRECIMIENTO")
        intercrec = (resultadox, "-∞,")
        print (intercrec)
        print ("DETERMINAMOS INTERVALO DE CRECIMIENTO")
        interdec = ("-∞,", resultadox)
        print (interdec)
    
menu ()