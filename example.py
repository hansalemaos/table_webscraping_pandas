import pandas
from PrettyColorPrinter import add_printer
import pandas as pd
tables=pd.read_html('https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250')
df=tables[0]
df=df.drop(columns=[df.columns[0], *df.columns[3:]])
df['Rank & Title']=df['Rank & Title'].str.replace(r'^\s*\d+\.\s*','',regex=True)
df['Rank & Title']=df['Rank & Title'].str.split(r'\s+\(')
df['Year']=df['Rank & Title'].str[-1].str.strip(')').astype('Int64')
df.to_excel('c:\\movies2.xlsx')
