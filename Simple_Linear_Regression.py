import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
dataset = pd.read_csv("L-R.csv");
# print(dataset)
x = dataset['Income']
y= dataset['Food Expenditure']
# print(x)
# print(y)




def estimate_coeff(x,y):
    n=np.size(x)
    print(n)
    # let's read mean of x and y
    m_x = np.mean(x)
    m_y = np.mean(y)

    ss_xy = np.sum(y*x)-n*m_y*m_x
    ss_xx= np.sum(x*x)-n*m_x*m_x
    b_1 = ss_xy / ss_xx
    b_0 = m_y - b_1*m_x

    return (b_0, b_1)

print( estimate_coeff(x, y) )

b=estimate_coeff(x,y)
def plot_regression_line(x, y, b):
    # plotting the actual scattered line
    plt.scatter(x, y, color = "m", marker="o", s=30)
    y_predicted = b[0]+ b[1]*x
    plt.scatter(x,y_predicted, color="g")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

plot_regression_line(x,y,b)