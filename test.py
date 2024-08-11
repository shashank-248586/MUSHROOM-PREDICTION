import pickle
import numpy as np
import pandas as pd

def sum(a,b):
    return str(int(a) + int(b))


model  = pickle.load(open("model.pkl",'rb'))
encodermodel = pickle.load(open("encodermodel.pkl",'rb'))
def fun(row):
    p = [i for i in row.values()]
    p=np.reshape(p,(1,22))
    x =encodermodel.transform(p)
    ans = model.predict(x)
    greed=""
    if(ans ==0):
        greed ="POISION"
    else:
        greed = "EDABLE"
    return greed
