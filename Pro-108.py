import random
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import csv
df = pd.read_csv("data213.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()],["Avg %"],show_hist= False)
fig.show()