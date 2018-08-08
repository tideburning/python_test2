from random import randint



# sinh ra 1 điểm 
#point la 1 set
points = {(randint(0, 40), randint(0, 40)) }

#khi dưới 1000 điểm
while len(points) < 1000:
    #thêm điểm vào tập hợp points
    #|= là phép thêm vào tập hợp, nếu trùng nó sẽ không ghi vào 
    points |= {(randint(0, 40), randint(0, 40))}

#chuyển set thành list rồi chuyển vào mảng numpy
listps = list(points)

import numpy as np
np.array(listps).dump(open('array.npy', 'wb'))

# load tập điểm vào
myArray = np.load(open('array.npy', 'rb'))

# hiển thị dỡ liệu = matholotp=lib

import matplotlib.pyplot as plt

def kmeans_display(X, label):
    #Tạo 1 vector chứa các cụm rồi tách ra 5 cụm
    X0 = X[label == 0, :]
    X1 = X[label == 1, :]
    X2 = X[label == 2, :]
    X3 = X[label == 3, :]
    X4 = X[label == 4, :]
        
    plt.plot(X0[:, 0], X0[:, 1], 'bo')
    plt.plot(X1[:, 0], X1[:, 1], 'go')
    plt.plot(X2[:, 0], X2[:, 1], 'ro')
    plt.plot(X3[:, 0], X3[:, 1], 'co')
    plt.plot(X4[:, 0], X4[:, 1], 'mo')

    
    plt.plot()
    plt.show()


from sklearn.cluster import KMeans

#Gọi số cụm và fit dữ liệu 
kmeans = KMeans(n_clusters=5).fit(myArray)
#print('Centers found by scikit-learn:')
#print(kmeans.cluster_centers_)
#Dự đoán các cụm
label = kmeans.predict(myArray)
#Hiển thị
kmeans_display(myArray, label)