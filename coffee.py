import plotly.express as px
import csv 
with open ("coffee.csv") as f:
    df = csv.DictReader(f)
    fig=px.scatter(df,x="Coffee in ml" ,y="Sleep in hours")
    fig.show()