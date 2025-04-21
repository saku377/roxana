# print("ingrese un numero")
# num =int(input())


# for i in range(num):
#     print("repeticiones" , i + 1)





# pide un numero al usuario y muestra la tabla de ese numero hasta el 10
# print ("ingrese un numero")
# num = int(input())
# for i in range (10):
#     print( num , " x " , i , "=" , i*num)



# print("ingrese la cantidad de notas")
# cant = int(input())
# suma=0
# for i in range (cant):
#         print("ingrese nota" , i+1)
#         nota =int(input())
#         suma =suma + nota 
#         # suma += nota
# prom =suma / cant 
# print ("el promedio es " , prom)
cantA=int(input("ingrese el numero de alumnos"))

for j in range(cantA):
    print("ingrese la cantidad de notas" , j+1 ,"del alumno", j+1)
    cant = int(input())
    suma=0
    for i in range (cant):
            print("ingrese nota" , i+1 , "del alumno" , j+1)
            nota =int(input())
            suma =suma + nota 
            # suma += nota
    prom =suma / cant 
    print ("el promedio es " , prom)
    




