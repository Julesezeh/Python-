import pandas as pd 
from sqlalchemy import create_engine

data_frame = pd.read_csv("population_total.csv")

engine = create_engine('sqlite:///newdb.db')

data_frame.to_sql('population',engine)

engine.execute("SELECT * FROM population").fetchall()
