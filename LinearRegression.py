import numpy as np
import matplotlib.pyplot as plt


print("LinearRegression.py Is now Successfully Imported.")

def plotLine(b, m, X, y):
    max_x = np.max(X) + 100
    min_x = np.min(X) - 100


    xplot = np.linspace(min_x, max_x, 1000)
    yplot = m * xplot + b 



    plt.plot(xplot, yplot, color='#58b970', label='Regression Line')

    plt.scatter(X,y)
    plt.axis([-10, 10, 0, 200])
    plt.show()



def hypothesis(b, m, x):
    return (m*x) + b  

def cost(b, m, X, y):
    costValue = 0 
    for (xi, yi) in zip(X, y):
        costValue += 0.5 * ((hypothesis(b, m, xi) - yi)**2)
    return costValue




def derivatives(b, m, X, y):
    db = 0
    dm = 0
    for (xi, yi) in zip(X, y):
        db += hypothesis(b, m, xi) - yi
        dm += (hypothesis(b, m, xi) - yi)*xi

    db /= len(X)
    dm /= len(X)

    return db, dm

def updateParameters(b, m, X, y, alpha):
    db, dm = derivatives(b, m, X, y)
    b = b - (alpha * db)
    m = m - (alpha * dm)

    return b, m
    
def LinearRegression(X, y):
    b = np.random.rand()
    m = np.random.rand()
    
    for i in range(0, 1000):
        if i % 100 == 0:
            plotLine(b, m, X, y)
        # print(cost(b, m, X, y))
        b, m = updateParameters(b, m, X, y, 0.005)



    


LinearRegression(X, y)