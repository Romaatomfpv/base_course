import numpy as np
from scipy import constants


g = constants.g  
k_B = constants.k 
h = constants.h  
e = np.e  


h_height = 10 
result_1 = np.sqrt(2 * g * h_height)
print(f"Значение первого выражения (sqrt(2 * g * h)): {result_1:.4f} м/с")


T = 300 
f = 1e12  
exponent = h * f / (k_B * T)
result_2 = k_B * T * np.exp(exponent)
print(f"Значение второго выражения (k_B * T * exp(h * f / (k_B * T))): {result_2:.4e} Дж")
