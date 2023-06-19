import pandas as pd
import matplotlib.pyplot as mo 
import numpy as np 
from decimal import *
getcontext().prec = 40
# đọc dữ liệu
data = pd.read_csv('data.csv',header = None)
#tách in và out ra thành 2 mảng 2 chiều
X = np.array([data.values[:,0]]).T #[in]
y = np.array([data.values[:,1]]).T #[out]

#tạo một mảng có kích thước như in với các giá trị bằng 1 [1]
one = np.ones((X.shape[0], 1))

#tạo mảng X mới bằng cách ghép 2 các cột của 2 mảng [1,in]
Xbar = np.concatenate((one, X), axis = 1)

#Tính hằng số m và b theo công thức
#nhân đảo chiều Xbar với chính nó 
A = np.dot(Xbar.T, Xbar)

#nhân Xbar với y
b = np.dot(Xbar.T, y)
#nhân ma trận giả ngịch đảo của A với b
w = np.dot(np.linalg.pinv(A), b)
b = w[0]
m = w[1]

minval = X[0][0]
maxval = X[0][0]
for i in X:
    if i < minval:
       minval = i
    if i > maxval:
       maxval = i
#tạo một mảng có 2 tham số min và max là 2 điểm đầu và cuối của đường trung bình
x0 = np.linspace(minval - 5, maxval + 5, 2)

#tính góc độ theo công thức
y0 = b + m*x0

#vẽ 
mo.plot(X.T, y.T, 'x')
mo.plot(x0, y0)            
mo.show()
input("press close to exit")