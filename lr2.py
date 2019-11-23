import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

datas=pd.read_csv("datasets/fish.csv") #Veri setimin yolunu belirliyorum

X=datas["Width"]  #Veri setimizden sütunlarımızı alıyoruz
Y=datas["Height"]

plt.plot(X,Y,"og")  #Verilerimizi nokta grafiği şeklinde çiziyoruz.

a,b = np.polyfit(X,Y,1) 
"""
X ve Y verilerine göre 1. dereceden bir polinom fit ediyoruz ve bu polinomun 
a, b değerlerini alıyoruz.
"""

plt.plot(X,a*X+b)  #Burada da aynı şekilde doğrumuzu çizdiriyoruz.
plt.show()