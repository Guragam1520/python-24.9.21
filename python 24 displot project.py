import pandas as pd
import plotly.figure_factory as ff
import csv

df= pd.read_csv("data 24.9.21 project.csv")
fig=ff.create_distplot([df["Avg Rating"].tolist()],["Avg Rating"],show_hist=False)
fig.show()
