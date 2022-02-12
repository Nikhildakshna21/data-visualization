import pandas as pd
import plotly.express as px

data = pd.read_csv('covid.csv')

fig = px.bar(data,x='date',y='cases',color='country')

fig.show()

