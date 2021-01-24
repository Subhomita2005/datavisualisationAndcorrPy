import plotly.express as px
import csv 
import numpy as np
def getDataSource(path) :
    icecream_sales=[]
    temperature_sales=[]
    with open(path) as f:
        csvreader=csv.DictReader(f)
        for row in csvreader:
            icecream_sales.append(float(row["Ice-cream Sales"]))
            temperature_sales.append(float(row["Temperature"]))
    return {"x":icecream_sales,"y":temperature_sales} 
def findcorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print(correlation[0,1]) 
def setup():
    path="icecream.csv"
    dataSource=getDataSource(path)
    findcorrelation(dataSource)
setup()        
