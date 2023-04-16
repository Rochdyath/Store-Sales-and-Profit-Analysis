import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import plotly.colors as colors
pio.templates.default = "plotly_white"

data = pd.read_csv("Superstore.csv", encoding='latin-1')

data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Ship Date'] = pd.to_datetime(data['Ship Date']) 
data['Order Month'] = data['Order Date'].dt.month
data['Order Year'] = data['Order Date'].dt.year
data['Order Day of Week'] = data['Order Date'].dt.dayofweek

def monthy_sales():
    df = data.groupby('Order Month').size().reset_index(name='sales')
    fig = px.line(df, y='counts', x='Order Month', title='Monthly sales')
    fig.show()

monthy_sales()