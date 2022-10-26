import pandas as pd
data = pd.read_csv("file_name.csv")
print(data.head())

import plotly.express as px
fig = px.box(data, y="TV")
fig.show()
