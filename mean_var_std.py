import numpy as np

def calculate(list):

    n = len(list)

    if n != 9 :
        raise ValueError("List must contain nine numbers.")
    
    else :
        a = np.array(list)
        a = a.reshape((3,3))

        newDict = {}
        newDict["mean"] = [np.mean(a,axis = 0).tolist(),np.mean(a,axis = 1).tolist(),np.mean(a)]
        newDict['variance'] = [np.var(a,axis =0).tolist(),np.var(a,axis =1).tolist(),np.var(a,)]
        newDict["standard deviation"] = [np.std(a,axis =0).tolist(),np.std(a,axis =1).tolist(),np.std(a)]
        newDict["max"] = [np.max(a,axis =0).tolist(),np.max(a,axis =1).tolist(),np.max(a)]
        newDict["min"] = [np.min(a,axis =0).tolist(),np.min(a,axis =1).tolist(),np.min(a)]
        newDict["sum"] = [np.sum(a,axis =0).tolist(),np.sum(a,axis =1).tolist(),np.sum(a)]

        return newDict