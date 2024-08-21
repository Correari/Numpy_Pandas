import numpy as np
arr = np.arange(0, 11)
print(arr)
trozo_de_arr = arr[0:6]
print(trozo_de_arr)
#A todo mi array le quiero quitar todos los valores y dejarlos en cero 
trozo_de_arr[:] = 0
print(trozo_de_arr)
#Si ahora imprimimor el array completo, veras que todos los valores han sido cambiados
print(arr)
#Para soluconar esto, utilizaremos el comando copy
arr_copy = arr.copy()
arr_copy[:] = 100
print(arr_copy)
#no obstante la lista original es respetada
print(arr)
