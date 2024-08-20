import numpy as np
#Definimos números aleatorios del 1 al 20 en un vector
arr = np.random.randint(1, 20, 10)
print(arr)
#Ahora lo llevamos a una estructura matricial
matriz = arr.reshape(2,5)
print(matriz)
#Con max voy a traer el numero mas grande que tenga nuestro arr
maximo = arr.max()
print(maximo)
#Crearemos un array de dos dimensiones 
a = np.array([[1, 2,], [3, 4,]])
b = np.array([[5, 6]])
#¿Qué pasa cuando quieres unir el array b con el array a
c = np.concatenate((a, b), axis=0)
print(c)
