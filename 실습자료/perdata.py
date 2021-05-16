import urllib.request as req
import pandas as pd

def make_perdata(firm_code) :
    
    fs_url = "https://comp.fnguide.com/SVO2/asp/SVD_Main.asp?pGB=1&cID=&MenuYn=Y&ReportGB=&NewMenuID=101&stkGb=701gicode=" + firm_code
    fs_page = req.urlopen(fs_url)
    fs_table = pd.read_html(fs_page)
    
    ## per data
    df_8= fs_table[8]
    df_8 = df_8.set_index(df_8.columns[0])
    df_8 = df_8[df_8.columns[:1]]
    df_8.columns = [firm_code ]
    temp = df_8.T
       
    
    return temp
