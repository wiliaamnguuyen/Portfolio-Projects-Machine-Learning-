# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 09:30:27 2018

@author: William X Nguyen
"""

import statsmodel.formula.api as sm
def backwardElimination(x,sl):
    numVars = len(x[0])
    for i in range(0,numVars):
        regressor_OLS = sm.OLS(y,x).fit()
        maxVar = max(regressor_OLS.pvalues).astype(float)
        if maxVar > sl:
            for j in range(0,numVars-i):
                if (regressor_OLS.pvalues[j].astype(float)==maxVAR):
                    x=np.delete(x,j,1)
    regressor_OLS.summary()
    return x

SL = 0.05
X_opt = X[:,[0,1,2,3,4,5]]
X_Modeled = backwardElimination(X_opt,SL)