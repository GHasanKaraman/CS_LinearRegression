import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

datas=pd.read_csv("datasets/fish.csv") #Veri setimin yolunu belirliyorum

X=np.array(datas["Width"]).reshape(-1,1)  #Veri setimizden sütunlarımızı alıyoruz
Y=np.array(datas["Height"]).reshape(-1,1)
"""
Verilerimize reshape fonksiyonunu uyguladık. Bunun sebebi verileri
direk aldığımızda 1xN boyutunda bir matris olarak almasındandır.
Yani verilerin yatay olmasıdır. [1,2,3,4,5] gibi
Eğer biz reshape(-1,1) yaparsak verilerimiz
[1
 2
 3
 4
 5]  gibi olur. Bunu yapmamızın sebebi scikit kütüphanesinin verileri
böyle istemesindendir.

"""

plt.plot(X,Y,"og")  #Verilerimizi nokta grafiği şeklinde çiziyoruz.

lr = LinearRegression() #Lineer Regresyon modelini oluşturuyoruz

lr.fit(X,Y) #X ve Y verilerine göre doğru fit ettik

a=lr.coef_[0][0]     #coefficient değerimizi yani katsayımızı alıyoruz
b = lr.intercept_[0] #intercept y eksenini kesen y değerini alıyoruz yani bias değerini

plt.plot(X,a*X+b)   #Aynı şekilde grafiğimizi çiziyoruz
plt.show()
