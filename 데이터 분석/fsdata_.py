import urllib.request as req
import pandas as pd
import fsdata

def make_fsdata(firm_code) :
    
    temp = fsdata.make_fsdata(firm_code)
    
    temp_ = temp.stack()
    temp_ = temp_.sort_index(level=1)
    temp = pd.DataFrame(temp_)
    temp = temp.T
    temp = temp.swaplevel(0,1,axis=1)
    temp_mt = temp.columns
    temp['firmcode'] = firm_code
    temp = temp.set_index('firmcode')
    temp.columns = temp_mt

    
    return temp
    
