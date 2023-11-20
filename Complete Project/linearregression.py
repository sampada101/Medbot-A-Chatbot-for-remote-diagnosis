import math
def estimateCofficient(x,y):
    sumx=0.0
    sumy=0.0
    sumxx=0.0
    sumxy=0.0
    
    for i in range(len(x)):
        sumx=sumx+x[i]
        sumy=sumy+y[i]
        sumxx=sumxx+x[i]*x[i]
        sumxy=sumxy+x[i]*y[i]
    
    # print("sumx: ",sumx)
    # print("sumy: ",sumy)
    # print("sumx2: ",sumxx)
    # print("sumxy: ",sumxy)
    
    return sumx, sumy, sumxx, sumxy
    
    
def calculateSlopem(N,sumx,sumy,sumxx,sumxy):
    val_xy=N*sumxy-sumx*sumy
    val_xx=N*sumxx-math.pow(sumx,2)
    m=val_xy/val_xx
    #m=round(m,3)
    
    return m
    
def calculateInterceptb(sumy,m,sumx,N):
    b=(sumy-m*sumx)/N
    b=round(b,3)
    
    return b

def regressionLine(m,x,b,N):
    
    y=0.0
    for i in range(len(x)):
        y=y+m*x[i]+b
    
    y=y/N            
    #y=round(y,3)
    
    return y
    
def initRegression(x,y):
    N=len(x)
    
    sumx,sumy,sumxx,sumxy=estimateCofficient(x,y)
    
    m=calculateSlopem(N,sumx,sumy,sumxx,sumxy)
    
    b=calculateInterceptb(sumy,m,sumx,N)
    y=regressionLine(m,x,b,N)
    
    
    return y
    
    
    
    
    