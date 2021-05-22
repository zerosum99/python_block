import urllib.request as req
import pandas as pd

def make_fsdata(firm_code) :
    
    fs_url = "https://comp.fnguide.com/SVO2/ASP/SVD_Finance.asp?pGB=1&cID=&MenuYn=Y&ReportGB=&NewMenuID=103&stkGb=701&gicode=" + firm_code
    fs_page = req.urlopen(fs_url)
    fs_table = pd.read_html(fs_page)
    
    ## 손익계산서 연결
    df_0= fs_table[0]
    df_0 = df_0.set_index(df_0.columns[0])
    df_pl = df_0[[*df_0.columns[:4]]]
    index = ["매출액","영업이익","당기순이익"]
    df_pl = df_pl.loc[index]
    
     ## 재무상태표 연결
    df_2= fs_table[2]
    df_2 = df_2.set_index(df_2.columns[0])
    df_bs = df_2[[*df_2.columns[:4]]]
    index = ["자산","부채","자본"]
    df_bs = df_bs.loc[index]
    
     ## 현금흐름표 연결
    df_4= fs_table[4]
    df_4 = df_4.set_index('IFRS(연결)')
    df_ii = df_4.loc[['영업활동으로인한현금흐름']]
    
    temp = pd.concat([df_pl, df_bs, df_ii])

    
    return temp
    
