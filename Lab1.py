
# program for Linear Regression 

 

# define the data lists and their lengths 

import math

xVals = [1, 2, 3, 4, 5, 6] 

yVals = [10, 12, 15, 13, 21, 19] 

m = len(xVals) 

n = len(yVals)  

# define a function to perform linear regression 

def LinReg() : 

    global xVals, yVals 

    global m, n 

    sumx = 0; sumy = 0; sumxy = 0; sumxx = 0; sumyy =0;

    slope = 0; yInt = 0 

   

    for index in range(n) : 

        sumx += xVals[index] 

        sumy += yVals[index] 

        sumxy += xVals[index] * yVals[index] 

        sumxx += xVals[index] * xVals[index] 

        sumyy += yVals[index] * yVals[index]  # add this line


    slope = (n * sumxy - sumx * sumy) / (n * sumxx - sumx * sumx)  

    yInt = (sumy * sumxx - sumx * sumxy) / (n * sumxx - sumx * sumx) 


    r = (n * sumxy - sumx * sumy) / (math.sqrt((n * sumxx - math.pow(sumx, 2)) * (n * sumyy - math.pow(sumy, 2)) ) )

    r2= math.pow(r, 2)
    

    if ( r >= 0.80 and r <= 1.00) : 

        print ("analysis: strong positive correlation") 

    if ( r <= -0.80 and r >= -1.00) : 

        print ("analysis: strong negative correlation") 

    if ( r > -0.80 and r < 0.80) : 

        print ("analysis: weak correlation")

      

    print ("the predicted slope is: %0.2f" % slope) 

    print ("the predicted intercept is: %0.2f" % yInt) 
    print ("") 

    print ("linear model: y = %0.2fx + %0.2f" % (slope, yInt)) 

    print ("") 

    # perform interpolation and extrapolation here 

    xInterp = 0
    yInterp = 0

    msg = "please provide an x-value for interpolation " 

    xInterp = float(input(msg))

    yInterp = slope * xInterp + yInt 

    print ("interpolation results: %0.2f" % yInterp)


    xExterp = 0
    yExterp = 0

    msg = "please provide an x-value for extrapolation " 

    xExterp = float(input(msg))

    yExterp = slope * xExterp + yInt 

    print ("Extrapolation results: %0.2f" % yExterp)

# call the Linear Regression function 

LinReg() 

 
