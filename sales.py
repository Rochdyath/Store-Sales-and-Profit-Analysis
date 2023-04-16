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
    df = data.groupby('Order Month')['Sales'].sum().reset_index(name='sales')
    fig = px.line(df, y='sales', x='Order Month', title='Monthly sales')
    fig.show()

def sales_by_category():
    df = data.groupby('Category')['Sales'].sum().reset_index(name='sales')
    fig = px.pie(df, values='sales', names='Category', hole=0.5,
                    title='Sales by category',
                    color_discrete_sequence=px.colors.qualitative.Set3)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(title_font=dict(size=24))
    fig.show()

def sales_by_subCategory():
    df = data.groupby('Sub-Category')['Sales'].sum().reset_index(name='sales')
    fig = px.bar(df, y='sales', x='Sub-Category', title='Sales by sub category')
    fig.show()

def monthly_profits():
    df = data.groupby('Order Month')['Profit'].sum().reset_index(name='profits')
    fig = px.line(df, y='profits', x='Order Month', title='Monthly profits')
    fig.show()

def profits_by_category():
    df = data.groupby('Category')['Profit'].sum().reset_index(name='profits')
    fig = px.pie(df, values='profits', names='Category', hole=0.5,
                    title='Profits by category',
                    color_discrete_sequence=px.colors.qualitative.Set3)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(title_font=dict(size=24))
    fig.show()

profits_by_category()