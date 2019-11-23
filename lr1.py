import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

datas=pd.read_csv("datasets/fish.csv") #Veri setimin yolunu belirliyorum

X=datas["Width"]  #Veri setimizden sütunlarımızı alıyoruz
Y=datas["Height"]

plt.plot(X,Y,"og")  #Verilerimizi nokta grafiği şeklinde çiziyoruz.

a=0  #ax+b doğrusu için başlangıç değeri atıyorum. İstenilen değer atanabilir.
b=0  #Genellikle y=0x+0 doğrusu başlangıç doğrusu kabul edilir.
learningRate=0.01  #Learning Rate değerimizi 0.01 olarak seçiyoruz.
epoch = 1000  #a ve b değerlerinin güncellenmesi için gerekli tekrar sayısı
#1000 kez verilerimiz eğitilecek

for i in range(epoch): #Döngümüz 1000 kez tekrar edecek
    
    _Y=a*X+b #doğrumuzun a*x+b olduğunu belirttik.
    
    """
    Ja değerimiz J'nin a'ya göre türevini temsil etmektedir. Biz bu 
    değeri zaten bulduğumuz için sadece buraya kod kısmına döküyoruz.
    (y-yi)xi  değerlerinin hepsini toplamamız gerektiği için sum 
    fonksiyonunu kullandık. Ardından formülden gelen -2/N ile bu
    bulduğumuz değeri çarptık.
    """
    Ja = ((Y-_Y)*X).sum()*(-2)/len(X)  
    
    
    Jb = (Y-_Y).sum()*(-2)/len(X)  #Burada da formülü uyguladık.
      
    
    #Burası da aynı şekilde güncelleme formüllerimizin uygulanmış hali
    a = a - Ja * learningRate
    b = b - Jb * learningRate
    
"""   
Eğitim bittikten sonra grafiğimizi çizdirelim. 
X,Y grafiğini çizdireceğiz. Y dediğimiz değer  
zaten ax+b olduğu için x,ax+b grafiğini çizdiriyoruz.
"""   
plt.plot(X,a*X+b)  
plt.show()
    